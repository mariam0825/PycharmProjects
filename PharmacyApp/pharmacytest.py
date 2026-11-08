
import unittest

from User import User
from Admin import Admin
from pharmacist import Pharmacist
from customer import Customer
from product import Product
from inventory import Inventory
from cart import Cart
from sale import Sale
from pharmacy import Pharmacy


class TestPharmacySystem(unittest.TestCase):

    def setUp(self):
        self.admin = Admin("Mariam", "admin", "pass123")
        self.pharmacist = Pharmacist("Aisha", "pharmacist", "pass456")
        self.customer = Customer("Fatima", "fatima", "pass789")
        self.product = Product(1, "Paracetamol", 500, 20, "2027-12-31")

        self.inventory = Inventory()
        self.inventory.add_product(self.product)

        self.cart = Cart()
        self.pharmacy = Pharmacy("Mariam Pharmacy")
        self.pharmacy.inventory = self.inventory

    # User tests
    def test_user_login_success(self):
        user = User("Mariam", "mariam", "1234")
        self.assertTrue(user.login("mariam", "1234"))

    def test_user_login_failure(self):
        self.assertFalse(self.admin.login("admin", "wrong"))

    # Admin tests
    def test_admin_add_product(self):
        new_product = Product(
            2, "Vitamin C", 1500, 10, "2027-06-30"
        )
        self.admin.add_product(self.inventory, new_product)

        self.assertIs(
            self.inventory.find_by_id(2), new_product
        )

    def test_admin_add_staff(self):
        self.admin.add_staff(self.pharmacist)
        self.assertIn(self.pharmacist, self.admin.staff)

    # Pharmacist tests
    def test_pharmacist_search_product(self):
        result = self.pharmacist.search_product(
            self.inventory, "paracetamol"
        )
        self.assertIs(result, self.product)

    def test_search_missing_product(self):
        result = self.inventory.search_product("Ibuprofen")
        self.assertIsNone(result)

    # Product tests
    def test_product_creation(self):
        self.assertEqual(self.product.name, "Paracetamol")
        self.assertEqual(self.product.price, 500)
        self.assertEqual(self.product.quantity, 20)

    def test_product_negative_price_rejected(self):
        with self.assertRaises(ValueError):
            Product(3, "Test", -100, 5, "2027-01-01")

    def test_update_product_price(self):
        self.product.update_price(600)
        self.assertEqual(self.product.price, 600)

    # Inventory tests
    def test_inventory_add_product(self):
        self.assertEqual(len(self.inventory.list_products()), 1)

    def test_duplicate_product_id_rejected(self):
        duplicate = Product(
            1, "Vitamin C", 1000, 5, "2027-06-30"
        )
        with self.assertRaises(ValueError):
            self.inventory.add_product(duplicate)

    def test_inventory_update_stock(self):
        self.inventory.update_stock(1, 5)
        self.assertEqual(self.product.quantity, 25)

    def test_inventory_prevents_negative_stock(self):
        with self.assertRaises(ValueError):
            self.inventory.update_stock(1, -25)

    # Cart tests
    def test_add_item_to_cart(self):
        self.cart.add_item(self.product, 2)
        self.assertEqual(self.cart.items[1], 2)

    def test_cart_calculate_total(self):
        self.cart.add_item(self.product, 3)
        self.assertEqual(
            self.cart.calculate_total(self.inventory), 1500
        )

    def test_cart_rejects_excess_quantity(self):
        with self.assertRaises(ValueError):
            self.cart.add_item(self.product, 21)

    def test_cart_rejects_zero_quantity(self):
        with self.assertRaises(ValueError):
            self.cart.add_item(self.product, 0)

    def test_remove_item_from_cart(self):
        self.cart.add_item(self.product, 2)
        self.cart.remove_item(1)
        self.assertEqual(self.cart.items, {})

    # Pharmacy and Sale tests
    def test_checkout_creates_sale(self):
        self.cart.add_item(self.product, 2)

        sale = self.pharmacy.checkout(
            self.customer, self.cart
        )

        self.assertEqual(sale.total, 1000)
        self.assertEqual(len(self.pharmacy.sales), 1)

    def test_checkout_deducts_stock(self):
        self.cart.add_item(self.product, 3)
        self.pharmacy.checkout(self.customer, self.cart)

        self.assertEqual(self.product.quantity, 17)

    def test_checkout_updates_purchase_history(self):
        self.cart.add_item(self.product, 1)
        self.pharmacy.checkout(self.customer, self.cart)

        self.assertEqual(len(self.customer.purchase_history), 1)

    def test_checkout_clears_cart(self):
        self.cart.add_item(self.product, 2)
        self.pharmacy.checkout(self.customer, self.cart)

        self.assertEqual(self.cart.items, {})

    def test_checkout_rejects_empty_cart(self):
        with self.assertRaises(ValueError):
            self.pharmacy.checkout(self.customer, self.cart)

    def test_sale_has_correct_item_details(self):
        self.cart.add_item(self.product, 2)
        sale = self.pharmacy.checkout(
            self.customer, self.cart
        )

        self.assertEqual(sale.items[0]["name"], "Paracetamol")
        self.assertEqual(sale.items[0]["quantity"], 2)
        self.assertEqual(sale.items[0]["subtotal"], 1000)

    def test_register_customer(self):
        self.pharmacy.register_customer(self.customer)
        self.assertIn(self.customer, self.pharmacy.customers)


if __name__ == "__main__":
    unittest.main()



