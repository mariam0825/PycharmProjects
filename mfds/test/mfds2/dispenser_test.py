import unittest

from src.mfds2.dispenser import Dispenser
from src.mfds2.fuel import Fuel


class DispenserTest(unittest.TestCase):
    def setUp(self):
        self.dispenser = Dispenser()
        self.dispenser.clear()

    def test_that_i_can_get_available_fuel(self):
        self.assertEqual({},self.dispenser.get_available_fuel())

    def test_add_fuel(self):
        self.dispenser.add_fuel("Petrol", 750, 700)
        self.assertEqual(1, self.dispenser.get_number_fuel_type_available())

    def test_that_i_can_get_the_price_per_litre(self):
        self.dispenser.add_fuel("Petrol", 750, 700)
        self.assertEqual(750, self.dispenser.get_price_per_litre("Petrol"))


    def test_that_i_can_update_the_price(self):
        self.dispenser.add_fuel("Petrol", 750, 700)
        self.assertEqual(750, self.dispenser.get_price_per_litre("Petrol"))
        self.dispenser.update_price("Petrol", 850)
        self.assertEqual(850, self.dispenser.get_price_per_litre("Petrol"))

    def test_that_i_can_restock(self):
        self.dispenser.add_fuel("Petrol", 750, 700)
        self.assertEqual(700, self.dispenser.get_available_fuel_quantity("Petrol"))
        self.dispenser.restock("Petrol", 300)
        self.assertEqual(1000, self.dispenser.get_available_fuel_quantity("Petrol"))

    def test_that_i_can_dispense_fuel_by_amount(self):
        self.dispenser.add_fuel("Petrol", 750, 700)
        self.assertEqual(700, self.dispenser.get_available_fuel_quantity("Petrol"))
        self.dispenser.dispense_with_amount("Petrol", 49500)
        self.assertEqual(634, self.dispenser.get_available_fuel_quantity("Petrol"))

    def test_that_i_can_dispense_fuel_by_quantity(self):
        self.dispenser.add_fuel("Petrol", 750, 700)
        self.assertEqual(700, self.dispenser.get_available_fuel_quantity("Petrol"))
        self.dispenser.dispense_with_quantity("Petrol", 66)
        self.assertEqual(634, self.dispenser.get_available_fuel_quantity("Petrol"))
