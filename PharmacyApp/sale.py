from datetime import datetime

class Sale:
    def __init__(self, sale_id, customer, items, total):
        self.sale_id = sale_id
        self.customer = customer
        self.items = items
        self.total = total
        self.date = datetime.now()

    def __str__(self):
        return (
            f"Sale #{self.sale_id} | "
            f"Customer: {self.customer.name} | "
            f"Total: ₦{self.total:.2f}"
        )
