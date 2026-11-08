
class Product:
    def __init__(self, product_id, name, price, quantity, expiry_date):
        if price < 0 or quantity < 0:
            raise ValueError("Price and quantity cannot be empty")
        self.product_id = product_id
        self.name = name
        self.price = price
        self.quantity = quantity
        self.expiry_date = expiry_date

    def update_price(self, new_price):
        if new_price < 0:
            raise ValueError("Price cannot be in negative value")
        self.price = new_price

    def receipt(self):
        return (
            f"Medicine: {self.name}\n"
            f"Price: ₦{self.price:.2f}\n"
            f"Stock: {self.quantity}"
        )

    def display_details(self):
        print(
            f"ID: {self.product_id} | Name: {self.name} | Price: ₦{self.price:.2f} | Stock: {self.quantity} | Expiry: {self.expiry_date}")