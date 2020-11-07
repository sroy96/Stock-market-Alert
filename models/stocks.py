class Stocks(object):
    def __init__(self, code: str, current_price: float, percentage_change: float, price_change: float, is_inc: bool,
                 is_dec: bool):
        self.code = code
        self.current_price = current_price
        self.percentage_change = percentage_change
        self.price_change = price_change
        self.is_inc = is_inc
        self.is_dec = is_dec

    def serializer(self):
        pass