from products import Product, NonStockedProduct, LimitedProduct
from typing import List

class Store:
    def __init__(self, products: List[Product]):
        """
        Initialize a Store instance with a list of products.
        Args:
            products (List[Product]): The initial list of products in the store.
        """
        self.products = products

    def add_product(self, product: Product):
        """
        Add a product to the store.
        Args:
            product (Product): The product to add.
        """
        self.products.append(product)

    def remove_product(self, product: Product):
        """
        Remove a product from the store.
        Args:
            product (Product): The product to remove.
        """
        self.products.remove(product)

    def get_total_quantity(self) -> int:
        """
        Get the total quantity of all products in the store.
        Returns:
            int: The total quantity of all products in the store.
        """
        total_quantity = 0
        for product in self.products:
            total_quantity += product.get_quantity()
        return total_quantity

    def get_all_products(self) -> List[Product]:
        """
        Get a list of all active products in the store.
        Returns:
            List[Product]: A list of all active products in the store.
        """
        active_products = []
        for product in self.products:
            if product.is_active():
                active_products.append(product)
        return active_products

    def order(self, shopping_list):
        """
        Place an order for the products in the shopping list and calculate the total price.
        Applies promotions to the products if applicable.
        Args:
            shopping_list (list): A list of tuples containing the products and quantities.
        Returns:
            float: The total price of the order.
        Raises:
            ValueError: If a product in the shopping list is not available in the store.
        """
        total_price = 0.0

        for product, quantity in shopping_list:
            if product in self.products and product.get_quantity() >= quantity:
                total_price += product.buy(quantity)
            else:
                raise ValueError(f"Insufficient quantity for product: {product.name}")

        return total_price
