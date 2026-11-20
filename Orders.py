from Product import Product
from OrderLine import OrderLine
from DiscountStrategy import DiscountStrategy, NoDiscount, BulkDiscount, PercentageDiscount, StudentDiscount

class Orders:
    def __init__(self, order_id:str, discount: DiscountStrategy):
        self.__order_id: str = order_id
        self.__order_lines: list[OrderLine] = []
        self.discount =  discount if discount is not None else NoDiscount()

    def add_order_line(self, product:Product, quantity: int) -> None:
        order_line = OrderLine(product,quantity)
        self.__order_lines.append(order_line)

    def remove_order_line(self, product:Product, quantity: int) -> None:
        for line in self.__order_lines:
            if line.product is product and line._quantity is quantity:
                self.__order_lines.remove(line)
                return True
        else:
            print("Order Line does not exist, unable to delete")
            return False
        
    def set_discount(self, discount: DiscountStrategy) -> None:
        self.discount = discount

    def calculate_total(self) -> float:
        # for line in self.__order_lines:
        #     print(line)
        total = sum(line.calculate_subtotal() for line in self.__order_lines)
        return self.discount.apply(total)



    
from Supplier import  Supplier
from PhysicalProduct import PhysicalProduct
from DigitalProduct import DigitalProduct

#Test composition
supplier1 = Supplier("S1", "Jarrel", "jarrel@gmail.com")
book = PhysicalProduct("Book", "P01", 50.0, 20, supplier1, 20.5, "physical")
ebook = DigitalProduct("E-Book", "P02", 15.0, 30, supplier1, 500.57, "digital")
order1 = Orders("Order1", StudentDiscount("student",10))


#Order 1
order1.add_order_line(book, -5)
print(order1.calculate_total())



