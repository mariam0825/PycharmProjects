import unittest
from pharmacist import Pharmacist
from inventory import Inventory
from product import Product


class TestPharmacist(unittest.TestCase):

    def setUp(self):
        self.pharmacist = Pharmacist("Aisha", "aisha", "1234" )
        self.inventory = Inventory()
        self.product = Product(1, "Paracetamol", 500, 20, "2027-12-31")
        self.inventory.add_product(self.product)

    def test_search_existing_product(self):
        result = self.pharmacist.search_product(self.inventory, "Paracetamol")
        self.assertIs(result, self.product)

    def test_search_missing_product(self):
        result = self.pharmacist.search_product(self.inventory, "Ibuprofen")
        self.assertIsNone(result)



