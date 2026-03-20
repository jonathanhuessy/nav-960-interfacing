from enum import Enum

class ProductId(Enum):
    Unknown = 0
    Buffalo = 1
    Radio = 2
    Ceres = 3
    Orca = 4
    Echo = 5
    Orff = 6
    Ahi = 7
    Pollux = 8
    Saturn = 9
    Wahoo = 10
    Manatee = 11
    RadioBlade = 12
    Shifter = 13
    Nickel = 14
    Whippet = 15

    @classmethod
    def getProductId(self, productStr):
        if productStr is None:
            return ProductId.Unknown

        for name, Product in ProductId.__members__.items(): # iterate over all defined types
            if productStr.upper() == name.upper():
                return Product

        return ProductId.Unknown

    # helper functions to resolve product "class"
    def isPicusProduct(self):
        return self.name in ["Orca", "Echo", "Orff", "Ahi", "Pollux", "Saturn", "Wahoo", "Manatee"]

    def isBuffaloProduct(self):
        return self.name in ["Buffalo"]

    def isFusionProduct(self):
        return self.name in ["Shifter","Nickel", "Whippet"]

    def isDemeterProduct(self):
        return self.name in ["Ceres"]
