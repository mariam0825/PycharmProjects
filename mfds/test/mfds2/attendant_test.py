import unittest
from src.mfds2.dispenser import Dispenser
from src.mfds2.fuel import Fuel
from src.mfds2.attendant import Attendant

class AttendantTest(unittest.TestCase):

    def setUp(self):
        self.dispenser = Dispenser()
        self.dispenser.clear()
        self.attendant = Attendant("Mariam", self.dispenser)

    def test_that_attendant_has_a_name(self):
        self.assertEqual("Mariam", self.attendant.attendant_name)

    def test_that_attendant_can_add_fuel(self):
        fuels = Fuel("Petrol", 750, 700)
        self.attendant.add_fuel("Petrol", 750, 700)
        self.assertEqual(1, self.dispenser.get_number_fuel_type_available())

    def test_that_attendant_can_get_available_fuel(self):
        fuels = Fuel("Petrol", 750, 700)
        self.attendant.add_fuel("Petrol", 750, 700)
        self.assertEqual(700, self.attendant.get_available_fuel()["Petrol"].quantity )

    def test_that_attendant_can_update_fuel_price(self):
        fuels = Fuel("Petrol", 750, 700)
        self.attendant.add_fuel("Petrol", 750, 700)
        self.attendant.update_fuel_price("Petrol", 850)
        self.assertEqual(850, self.dispenser.get_price_per_litre("Petrol"))

    def test_that_attendant_can_restock_fuel(self):
        fuels = Fuel("Petrol", 750, 700)
        self.attendant.add_fuel("Petrol", 750, 700)
        self.attendant.restock_fuel("Petrol", 300)
        self.assertEqual(1000, self.dispenser.get_available_fuel_quantity("Petrol"))

    def test_that_attendant_can_dispense_fuel_by_litres(self):
        fuels = Fuel("Petrol", 750, 700)
        self.attendant.add_fuel("Petrol", 750, 700)
        self.attendant.dispense_fuel_by_liters("Petrol", 2)
        self.assertEqual(698, self.dispenser.get_available_fuel_quantity("Petrol"))

    def test_that_attendant_can_dispense_fuel_by_amount(self):
        fuels = Fuel("Petrol", 750, 700)
        self.attendant.add_fuel("Petrol", 750, 700)
        self.attendant.dispense_fuel_by_amount("Petrol", 1500)
        self.assertEqual(698, self.dispenser.get_available_fuel_quantity("Petrol"))

    def test_that_attendant_can_show_all_transactions(self):
        fuels = Fuel("Petrol", 750, 700)
        self.attendant.add_fuel("Petrol", 750, 700)
        self.attendant.dispense_fuel_by_liters("Petrol", 6)
        transactions = self.attendant.show_all_transactions()
        self.assertEqual(1, len(transactions))
        self.assertEqual("Petrol", transactions[0]["fuel_name"])
        self.assertEqual(6, transactions[0]["litres"])



