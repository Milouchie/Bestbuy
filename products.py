from abc import ABC, abstractmethod
import math

class Product:
    def __init__(self, name, price, quantity):
        """
        Initialize a Product instance.
        Args:
            name (str): The name of the product.
            price (float): The price of the product.
            quantity (int): The quantity of the product.
        """
        if not name:
            raise ValueError("Product name cannot be empty.")
        if price < 0:
            raise ValueError("Product price cannot be negative.")

        self.name = name
        self.price = price
        self.quantity = quantity
        self.active = True
        self.promotion = None

    def get_quantity(self):
        """
        Get the quantity of the product.
        Returns:
            int: The quantity of the product.
        """
        return self.quantity

    def is_active(self):
        """
        Check if the product is active.
        Returns:
            bool: True if the product is active, False otherwise.
        """
        return self.active

    def show(self):
        """
        Display information about the product.
        Returns:
            str: Information about the product.
        """
        promotion_info = f", No promotion"
        if self.promotion:
            promotion_info = f", Promotion: {self.promotion.name}"
        return f"{self.name}: ${self.price} ({self.quantity} available){promotion_info}"

    def buy(self, quantity):
        """
        Buy a specified quantity of the product.
        Args:
            quantity (int): The quantity to buy.
        Returns:
            float: The total price of the purchase.
        Raises:
            ValueError: If the product is not active or there is not enough quantity available.
        """
        if not self.active:
            raise ValueError("Product is not active")
        if quantity > self.quantity:
            raise ValueError("Not enough quantity available")

        if self.promotion:
            total_price = self.promotion.apply_promotion(self, quantity)
        else:
            total_price = self.price * quantity

        self.quantity -= quantity

        if self.quantity == 0:
            self.deactivate()

        return total_price

    def set_quantity(self, quantity):
        """
        Set the quantity of the product.
        Args:
            quantity (int): The quantity to set.
        """
        self.quantity = quantity
        if self.quantity <= 0:
            self.active = False
        else:
            self.active = True
        if self.quantity <= 0:
            self.deactivate()
        else:
            self.activate()

    def activate(self):
        """Activate the product."""
        self.active = True

    def deactivate(self):
        """Deactivate the product."""
        self.active = False

    def set_promotion(self, promotion):
        """
        Set a promotion for the product.
        Args:
            promotion (Promotion): The promotion to set.
        """
        self.promotion = promotion


class Promotion(ABC):
    def __init__(self, name):
        self.name = name

    @abstractmethod
    def apply_promotion(self, product, quantity):
        pass

class SecondHalfPrice(Promotion):
    def __init__(self, name):
        super().__init__(name)

    def apply_promotion(self, product, quantity):
        num_full_price_items = quantity // 2
        num_discounted_items = quantity - num_full_price_items
        total_price = (num_full_price_items * product.price) + (num_discounted_items * (product.price / 2))
        return total_price



class ThirdOneFree(Promotion):
    def __init__(self, name):
        super().__init__(name)

    def apply_promotion(self, product, quantity):
        return (quantity // 3 * 2 + quantity % 3) * product.price


class PercentDiscount(Promotion):
    def __init__(self, name, percent):
        super().__init__(name)
        self.percent = percent

    def apply_promotion(self, product, quantity):
        return product.price * quantity * (1 - self.percent / 100)


class NonStockedProduct(Product):
    def __init__(self, name, price):
        """
        Initialize a NonStockedProduct instance.
        Args:
            name (str): The name of the product.
            price (float): The price of the product.
        """
        super().__init__(name, price, quantity=float('inf'))
        self.promotion = None  # Add a default promotion attribute

    def show(self):
        """
        Returns a string representation of the product including its name, price, quantity, and promotion (if applicable).
        """
        promotion = getattr(self, 'promotion', None)
        promotion_info = f", Promotion: {promotion.name}" if promotion else ", No promotion"
        return f"{self.name}: ${self.price} (unlimited available){promotion_info}"


class LimitedProduct(Product):
    def __init__(self, name, price, quantity, max_quantity, promotion=None):
        super().__init__(name, price, quantity)
        self.max_quantity = max_quantity
        self.promotion = promotion

    def show(self):
        """
        Returns a string representation of the product including its name, price, quantity, and promotion (if applicable).
        """
        promotion = getattr(self, 'promotion', None)
        promotion_info = f", Promotion: {promotion.name}" if promotion else ", No promotion"
        return f"{self.name}: ${self.price} ({self.quantity} available){promotion_info}"

