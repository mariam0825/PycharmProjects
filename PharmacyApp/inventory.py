class Inventory:
    def __init__(self):
        self.products = {}

    def add_product(self, product):
        if product.product_id in self.products:
            print("Product ID already exists.")
            return
        self.products[product.product_id] = product
        print("Product added successfully.")

    def reduce_quantity(self, product_id, quantity):
        if product_id in self.products:
            self.products[product_id].quantity -= quantity
        else:
            print("Product not found.")

    def view_inventory(self):
        if not self.products:
            print("No products available.")
            return
        for product in self.products.values():
            product.display_details()
            print("-" * 30)