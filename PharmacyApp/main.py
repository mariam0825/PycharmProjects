from datetime import datetime, date
from pharmacy import Pharmacy
from inventory import Inventory
from product import Product
from Admin import Admin
from pharmacist import Pharmacist
from User import User
from cart import Cart

FILENAME = "products.txt"

def load_products(inventory):
    try:
        with open(FILENAME, "r") as file:
            for filename in file:
                if filename.strip():
                    product, name, price, qty, expiry = filename.strip().split(",")
                    expiry_date = datetime.strptime(expiry, "%Y-%m-%d").date()
                    product = Product(product, name, float(price), int(qty), expiry_date)
                    inventory.products[product] = product
    except FileNotFoundError:
        pass


def save_product(product):
    with open(FILENAME, "a") as file:
        file.write(f"{product.product_id},{product.name},{product.price},{product.quantity},{product.expiry_date}\n")


def main():
    pharmacy = Pharmacy("Mariam Pharmacy")
    load_products(pharmacy.inventory)

    while True:
        print("\n=== 💊 MARIAM PHARMACY SYSTEM ===")
        print("1. Admin Portal")
        print("2. Pharmacist Portal")
        print("3. Customer Portal")
        print("4. Exit")
        choice = input("\nSelect a portal (1-4): ").strip()

        match choice:
            case "1":
                print("\n--- Admin Login ---")
                admin = Admin(input("Name: "), input("Username: "), input("Password: "))

                while True:
                    print(f"\nWelcome {admin.name} to admin Portal")
                    print("1. Add Product\n2. View Inventory\n3. Back")
                    action = input("Choose (1-3): ").strip()

                    match action:
                        case "1":
                            try:
                                product = Product(
                                    product_id=input("Product ID: "),
                                    name=input("Name: "),
                                    price=float(input("Price (₦): ")),
                                    quantity=int(input("Quantity: ")),
                                    expiry_date=date(int(input(" Expiry Date ,Year (YYYY): ")), int(input("Month (MM): ")),
                                                     int(input("Day (DD): ")))
                                )
                                admin.add_product(pharmacy.inventory, product)
                                save_product(product)
                                print("Product saved successfully.")
                            except ValueError as e:
                                print(f"Input error: {e}")
                        case "2":
                            pharmacy.inventory.view_inventory()
                        case "3":
                            break
                        case _:
                            print("Invalid choice.")

            case "2":
                print("\n--- Pharmacist Login ---")
                pharmacist = Pharmacist(input("Name: "), input("Username: "), input("Password: "))

                while True:
                    print(f"\nWelcome Pharmacist {pharmacist.name}")
                    print("1. Search Product\n2. Check Expiry\n3. Back")
                    action = input("Choose (1-3): ").strip()

                    match action:
                        case "1":
                            pid = input("Enter Product ID: ").strip()
                            product = pharmacy.inventory.find_by_id(pid)
                            print(product.receipt() if product else "Product not found.")
                        case "2":
                            pid = input("Enter Product ID: ").strip()
                            product = pharmacy.inventory.find_by_id(pid)
                            print(f"Expires on: {product.expiry_date}" if product else "Product not found.")
                        case "3":
                            break
                        case _:
                            print("Invalid choice.")

            case "3":
                print("\n--- User Setup ---")
                customer = User(input("Your Name: "), input("Your Email: "))
                pharmacy.register_customer(customer)
                cart = Cart()

                while True:
                    print(f"\nWelcome Customer {customer.name}")
                    print("1. Browse Inventory\n2. Add to Cart\n3. Checkout\n4. Back")
                    action = input("Choose (1-4): ").strip()

                    match action:
                        case "1":
                            pharmacy.inventory.view_inventory()
                        case "2":
                            product= input("Product ID do you want to buy: ").strip()
                            qty = int(input("Enter Quantity: "))
                            product = pharmacy.inventory.find_by_id(product)
                            if product:
                                cart.add_item(product, qty)
                                print(f"Added {qty}x {product.name} to cart.")
                            else:
                                print("Product not found.")
                        case "3":
                            if not cart.items:
                                print("Your cart is empty.")
                            else:
                                try:
                                    sale = pharmacy.checkout(customer, cart)
                                    print("\nCheckout Successful!\n", sale)
                                except ValueError as e:
                                    print(f"Checkout failed: {e}")
                        case "4":
                            break
                        case _:
                            print("Invalid choice.")

            case "4":
                print("\nThank you for Using Maraiam pharmacy!!!")
                break
            case _:
                print("Please choose between 1 and 4.")


if __name__ == "__main__":
    main()