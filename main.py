import products
import store

def start(store_obj):
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
            products = store_obj.get_all_products()
            for product in products:
                print(product.show())

        elif choice == "2":
            total_quantity = store_obj.get_total_quantity()
            print(f"\nTotal amount in store: {total_quantity}")

        elif choice == "3":
            shopping_list = []
            products = store_obj.get_all_products()
            print("\nAvailable products:")
            for index, product in enumerate(products):
                print(f"{index+1}. {product.name}")
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

            try:
                total_price = store_obj.order(shopping_list)
                print(f"\nOrder placed successfully. Total price: {total_price}")
            except Exception as e:
                print(f"\nOrder failed: {str(e)}")

        elif choice == "4":
            print("Thank you for using the Store. Goodbye!")
            break

        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    # Setup initial stock of inventory
    product_list = [products.Product("MacBook Air M2", price=1450, quantity=100),
                    products.Product("Bose QuietComfort Earbuds", price=250, quantity=500),
                    products.Product("Google Pixel 7", price=500, quantity=250)
                    ]
    best_buy = store.Store(product_list)
    start(best_buy)
