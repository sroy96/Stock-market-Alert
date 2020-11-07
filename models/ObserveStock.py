from interfaces.interface import StockToObserve
from abc import ABC


class StockObserve(StockToObserve, ABC):
    def __init__(self):
        pass

    def serialize(self):
        serialized_output = {
            "user_email": self.user_email,
            "stock_exchange_name": self.stock_exchange_name,
            "nse_code": self.nse_code,
            "target": self.target,
            "stop_loss": self.stop_loss,
            "set_percentage_margin": self.set_percent_margin
        }
        return serialized_output
