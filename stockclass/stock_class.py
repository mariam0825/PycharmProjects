class stock:
    def __init__(self, symbol, current_price):
        self.symbol = symbol
        self.current_price = current_price

    @property
    def current_price(self):
        return self.current_price

    @current_price.setter
    def current_price(self, amount):
        if amount < 0:
            raise ValueError("balance can't be negative")
        self.current_price = amount