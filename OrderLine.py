from Product import Product

class OrderLine:
    def __init__(self, product, quantity):
        self.product:Product = product
        self._quantity:int = quantity
        self._productname:str = product.name
        pass

    def line_total(self) -> float:
        return self._quantity * self.product._price

    def __str__(self):
        return f"{self._productname} -------------------- x{self._quantity}"

    def __repr__(self):
        return self.__str__()