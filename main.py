from products import Product, NonStockedProduct, LimitedProduct, SecondHalfPrice, ThirdOneFree, PercentDiscount
from store import Store

def make_order(store_obj):
    """
    Function to facilitate the process of making an order.
    Takes a Store object as input and prompts the user to select products and quantities for the order.
    """
    shopping_list = []
    products = store_obj.get_all_products()
    print("\nAvailable products:")
    for index, product in enumerate(products):
        print(f"{index + 1}. {product.name}")
    print("Enter 'done' to finish adding products to the order.")

    while True:
        selection = input("Enter product number to add to the order: ")
        if selection == "done":
            break
        try:
            product_index = int(selection) - 1
            if product_index < 0 or product_index >= len(products):
                print("Invalid product number. Please try again.")
            else:
                quantity = input("Enter quantity: ")
                shopping_list.append((products[product_index], int(quantity)))
        except ValueError:
            print("Invalid input. Please enter a number.")

    if shopping_list:
        try:
            total_price = store_obj.order(shopping_list)  # Update the method name
            print(f"\nOrder placed successfully. Total price: {total_price}")
        except ValueError as e:
            print(f"\nOrder failed: {str(e)}")
    else:
        print("No products added to the order.")


def main():
    """
    Main function to run the Store application.
    Displays a menu and prompts the user to choose an option.
    """
    # Setup initial stock of inventory
    product_list = [
        Product("MacBook Air M2", price=1450, quantity=100),
        Product("Bose QuietComfort Earbuds", price=250, quantity=500),
        Product("Google Pixel 7", price=500, quantity=250),
        NonStockedProduct("Windows License", price=125),
        LimitedProduct("Shipping", price=10, quantity=250, max_quantity=1)
    ]

    # Create promotion catalog
    second_half_price = SecondHalfPrice("Second Half price!")
    third_one_free = ThirdOneFree("Third One Free!")
    thirty_percent = PercentDiscount("30% off!", percent=30)

    # Set promotions for products
    product_list[0].set_promotion(second_half_price)
    product_list[1].set_promotion(third_one_free)
    product_list[3].set_promotion(thirty_percent)

    # Create Store instance
    best_buy = Store(product_list)

    while True:
        print("\nWelcome to the Store!")
        print("Please select an option:")
        print("1. List all products in store")
        print("2. Show total amount in store")
        print("3. Make an order")
        print("4. Quit")

        choice = input("Enter your choice (1-4): ")

        if choice == "1":
            print("\nAll products in store:")
            products = best_buy.get_all_products()
            for product in products:
                print(product.show())

        elif choice == "2":
            total_quantity = best_buy.get_total_quantity()
            print(f"\nTotal amount in store: {total_quantity}")

        elif choice == "3":
            make_order(best_buy)

        elif choice == "4":
            print("Thank you for using the Store. Goodbye!")
            break

        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    # Run the Store application
    main()
