class Product:
    def __init__(self, name, price, quantity):
        if not name:
            raise ValueError("Invalid product name")
        if price < 0:
            raise ValueError("Invalid product price")
        if quantity < 0:
            raise ValueError("Invalid product quantity")

        self.name = name
        self.price = price
        self.quantity = quantity
        self.active = True

    def get_quantity(self):
        return self.quantity

    def set_quantity(self, quantity):
        self.quantity = quantity
        if self.quantity == 0:
            self.deactivated()

    def is_active(self):
        return self.active

    def activate(self):
        self.active = True

    def deactivate(self):
        self.active = False

    def show(self):
        return f"{self.name}, Price: {self.price}, Quantity: {self.quantity}"

    def buy(self, quantity):
        if not self.active:
            raise ValueError("Product is not active")
        if quantity > self.quantity:
            raise ValueError("Not enough quantity available")

        self.quantity -= quantity
        if self.quantity == 0:
            self.deactivate()

        return self.price * quantity

