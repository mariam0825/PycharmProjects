from User import User

class Admin(User):
    def __init__(self, name, username, password):
        super().__init__(name, username, password)
        self.staff = []
    def add_product(self, inventory, product):
        inventory.add_product(product)
    def add_staff(self, staff_member):
        self.staff.append(staff_member)