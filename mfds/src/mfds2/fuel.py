class Fuel:
    def __init__(self, name, amount_per_litre, quantity):
        self.fuel_name = name
        self.amount_per_litre = amount_per_litre
        self.quantity = quantity

    def get_name(self):
        return self.fuel_name

    def set_name(self, name):
        self.fuel_name = name

    def get_amount_per_litre(self):
        return self.amount_per_litre

    def set_amount_per_litre(self, amount_per_litre):
        self.amount_per_litre = amount_per_litre

    def get_quantity(self):
        return self.quantity

    def update_quantity(self, quantity):
        self.quantity += quantity

    def sell(self, quantity):
        self.quantity -= quantity