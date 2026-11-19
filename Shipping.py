#Imports
from abc import ABC, abstractmethod

#CanBeShipped Interface
class CanBeShipped(ABC):
    @abstractmethod
    def calculate_shipping_cost(self):
        pass