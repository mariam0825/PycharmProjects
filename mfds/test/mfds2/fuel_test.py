import unittest

from src.mfds2.fuel import Fuel


class MyTestCase(unittest.TestCase):
    def test_for_create_fuel(self):
        fuel = Fuel("Petrol","550", 400)
        self.assertEqual("Petrol", fuel.get_name())  # add assertion here

    # de

if __name__ == '__main__':
    unittest.main()
