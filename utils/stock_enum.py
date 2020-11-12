from interfaces.interface import Resource
from enum import Enum


class Code(object):
    enum = {"RELIANCE": "RI",
            "CIPLA": "C",
            "BIOCON": "BL03",
            "AXISBANK": "UTI10",
            "HDFCBANK": "HDF01",
            "BAJFINANCE": "BAF",
            "HEROMOTOCO": "HHM",
            "DIVISLAB": "DL03",
            "KOTAKBANK":"KMB",
            "HINDALCO":"HI",
            "M&M": "MM",
            "ITC": "ITC"
            }

    @staticmethod
    def stock_code_scrap(code):
        return Code.enum[code]
