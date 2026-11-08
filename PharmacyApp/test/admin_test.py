import unittest
from Admin import Admin
from pharmacist import Pharmacist
from inventory import Inventory
from product import Product


class TestAdmin(unittest.TestCase):

    def setUp(self):
        self.admin = Admin("Mariam", "admin", "1234")
        self.inventory = Inventory()
        self.product = Product(1, "Paracetamol", 500, 20, "2027-12-31")
        self.pharmacist = Pharmacist("Aisha", "aisha", "5678")

    def test_add_product(self):
        self.admin.add_product(self.inventory, self.product)
        self.assertIs(self.inventory.find_by_id(1), self.product )

    def test_add_staff(self):
        self.admin.add_staff(self.pharmacist)
        self.assertIn(self.pharmacist, self.admin.staff)


