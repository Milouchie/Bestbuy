from products import Product
from typing import List

class Store:
    def __init__(self, products: List[Product]):
        self.products = products

    def add_product(self, product: Product):
        self.products.append(product)

    def remove_product(self, product: Product):
        self.products.remove(product)

    def get_total_quantity(self) -> int:
        total_quantity = 0
        for product in self.products:
            total_quantity += product.get_quantity()
        return total_quantity

    def get_all_products(self) -> List[Product]:
        active_products = []
        for product in self.products:
            if product.is_active():
                active_products.append(product)
        return active_products

    def order(self, shopping_list: List[tuple]) -> float:
        total_price = 0
        for item in shopping_list:
            product, quantity = item
            if product not in self.products or not product.is_active():
                raise ValueError(f"Invalid product: {product_name}")
            if quantity > product.get_quantity():
                raise ValueError(f"Not enough quantity available for product: {product_name}")

            total_price += product.buy(quantity)

        return total_price

