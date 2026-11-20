from abc import ABC, abstractmethod

class DiscountStrategy(ABC):
    @abstractmethod
    def apply(self, total: float) -> float:
        pass

        

class NoDiscount(DiscountStrategy):
    def apply(self, total: float) -> float:
        return total

class PercentageDiscount(DiscountStrategy):
    def __init__(self, discount):
        self.discount = discount

    def apply(self,total:float, ) -> float:
        discount = total* self.discount/100
        total -= discount
        return total 
        

class BulkDiscount(DiscountStrategy):
    def __init__(self, threshold, discount): 
        self.threshold = threshold
        self.discount = discount

    def apply(self, total) -> float:
        if total >= self.threshold:
            total -= total * self.discount/100
            return total

class StudentDiscount(DiscountStrategy):
    def __init__(self, student, discount):
        self.age = student
        self.discount = discount

    def apply(self, total) -> float:
        if self.age == "student":
            total -= total * self.discount/100 
            return total
