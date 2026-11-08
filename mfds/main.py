from mfds2.dispenser import Dispenser
from mfds2.attendant import Attendant

dispenser = Dispenser()
attendant = Attendant("Mariam", dispenser)

menu = """
===== Welcome to Mariam Fuel Station! =====
    1. Add Fuel
    2. Sell Fuel
    3. History
    0. Exit
"""

while True:
    print(menu)
    choice = int(input("Enter your choice: "))

    match choice:
        case 1:
            fuel_name = input("Enter Fuel Name: ")
            price_per_litre = float(input("Enter Price per Litre: "))
            quantity = int(input("Enter Quantity available: "))

            if attendant.add_fuel(fuel_name, price_per_litre, quantity):
                print("Fuel is added successfully.")
            else:
                print("Fuel exists already.")

        case 2:
            available_fuel = dispenser.get_available_fuel()
            if not available_fuel:
                print("Fuel not available. Please add fuel first.")
            else:
                fuel_list = list(available_fuel.keys())
                for index, fuel_name in enumerate(fuel_list):
                    fuel = available_fuel[fuel_name]
                    print(f"{index}. Fuel Name: {fuel.get_name()} | "f"Price per litre: {fuel.get_amount_per_litre()}")

                fuel_name = input("Which type of fuel do you want to buy? ")
                if fuel_name not in available_fuel:
                    print("Fuel not available.")
                    continue

                print("""
                1. Buy with litres
                2. Buy with amount
                """)
                buy_choice = input(" How do you want to you want buy: ")
                if buy_choice == "1":
                    litres = float(input("How many litres do you want to buy: "))
                    total_amount = attendant.dispense_fuel_by_liters(fuel_name, litres)

                    if total_amount is not False:
                        print("Fuel sold successfully.")
                        print("Fuel:", fuel_name)
                        print("Litres purchased:", litres)
                        print("Total cost:", total_amount)
                    else:
                        print("Fuel sales  failed. Check the quantity available.")

                elif buy_choice == "2":
                    amount = float(input("Enter the amount you want to spend: "))
                    litres = attendant.dispense_fuel_by_amount(fuel_name, amount)

                    if litres is not False:
                        print("Fuel sold successfully.")
                        print("Fuel:", fuel_name)
                        print("Litres purchased:", litres)
                        print("Amount paid:", amount)
                    else:
                        print("Sale failed. Check the amount and quantity available.")
                else:
                    print("Invalid purchase option.")
        case 3:
            history = dispenser.show_all_transactions()
            if history:
                for transaction in history:
                    print(transaction)
            else:
                print("No transaction history available.")
        case 0:
                print("Thank you for visiting Mariam Fuel Station!")
                break
        case _:
            print("Invalid choice.")


