
class Attendant:
    def __init__(self, name, dispenser):
        self.attendant_name = name
        self.dispenser = dispenser

    def add_fuel(self, fuel_name, price, quantity):
        return self.dispenser.add_fuel(fuel_name, price, quantity)

    def get_available_fuel(self):
        return self.dispenser.get_available_fuel()

    def update_fuel_price(self, fuel_name, new_price):
        return self.dispenser.update_price(fuel_name, new_price)

    def restock_fuel(self, fuel_name, quantity):
        return self.dispenser.restock(fuel_name, quantity)

    def dispense_fuel_by_liters(self, fuel_name, litres):
        return self.dispenser.dispense_with_quantity(fuel_name, litres)

    def dispense_fuel_by_amount(self, fuel_name, amount):
        return self.dispenser.dispense_with_amount(fuel_name, amount)

    def show_all_transactions(self):
        return self.dispenser.show_all_transactions()