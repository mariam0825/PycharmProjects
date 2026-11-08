from User import User

class Pharmacist(User):
    def __init__(self, name, username, password,):
        super().__init__(name, username, password, role="Pharmacist")

    def search_product(self, inventory, product_name):
        return inventory.search_product(product_name)

    def check_for_expiry_date(self, inventory, product_name):
        return inventory.check_for_expiry_date(product_name)
