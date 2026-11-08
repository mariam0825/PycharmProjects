from inventory import Inventory
from sale import Sale

class Pharmacy:
    def __init__(self, name):
        self.name = name
        self.inventory = Inventory()
        self.customers = []
        self.sales = []
        self.next_sale_id = 1

    def register_customer(self, customer):
        self.customers.append(customer)

    def checkout(self, customer, cart):
        if not cart.items:
            raise ValueError("Cart is empty")

        total = cart.calculate_total(self.inventory)
        products = []
        for product_id, quantity in cart.items.items():
            product = self.inventory.find_by_id(product_id)
            if product is None:
                raise ValueError("Product not found")
            if quantity > product.quantity:
                raise ValueError("Insufficient stock")
            products.append((product, quantity))

        sale_items = []
        for product, quantity in products:
            sale_items.append({
                "product_id": product.product_id,
                "name": product.name,
                "quantity": quantity,
                "unit_price": product.price,
                "subtotal": product.price * quantity
            })

        for product, quantity in products:
            self.inventory.update_stock(product.product_id, -quantity)

        sale = Sale(self.next_sale_id, customer, sale_items, total)
        self.sales.append(sale)

        self.next_sale_id += 1
        cart.clear()

        return sale