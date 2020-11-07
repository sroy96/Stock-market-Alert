from interfaces.interface import Resource
from enum import Enum


class Code(object):
    enum = {"RELIANCE": "RI"
            }

    @staticmethod
    def stock_code_scrap(code):
        return Code.enum[code]
