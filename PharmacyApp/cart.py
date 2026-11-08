class Cart:
    def __init__(self):
        self.items = {}

    def add_item(self, product, quantity):
        if quantity <= 0:
            raise ValueError("Quantity must not be Zero")
        current_quantity = self.items.get(product.product_id, 0)
        if current_quantity + quantity > product.quantity:
            raise ValueError("Product not available")
        self.items[product.product_id] = current_quantity + quantity

    def remove_item(self, product_id):
        self.items.pop(product_id, None)

    def calculate_total(self, inventory):
        total = 0
        for product_id, quantity in self.items.items():
            product = inventory.find_by_id(product_id)
            if product is None:
                raise ValueError("Product not found")
            total += product.price * quantity
        return total

    def delete(self):
        self.items.clear()
