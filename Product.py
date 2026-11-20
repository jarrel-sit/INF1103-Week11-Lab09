#Imports
import math
from abc import ABC, abstractmethod
from Supplier import Supplier

#Creating Products(Blueprint)
class Product:
    def __init__(self, name: str, itemid: str, price: float, stock: int, supplier: Supplier):
        self.name = name
        self.itemid = itemid
        self._price = price
        self.stock = stock
        self.supplier: Supplier = supplier

    #Displays the information
    @abstractmethod
    def display_information(self):
        pass
        #print(f"Product ID: {self.itemid}\nProduct Name: {self.name}\nPrice: {self._price}\nStock: {self.stock}\n")

    #Abstract Method for fulfilment information of product that will be overwritten by child classes PhysicalProduct and DigitalProduct
    @abstractmethod
    def get_fulfilment_info(self):
        pass

    #Formats Product Details into dictionary format to load as json as Object cannot be stored in JSON
    @abstractmethod
    def to_dict(self):
        pass

    #String formatting
    def __str__(self):
            return self.display_information()

    def _base_info(self):
        return f"Product ID: {self.itemid}\nProduct Name: {self.name}\nPrice: {self._price}\nStock: {self.stock}\n"
    
    #Update stock method that can be inherited by child classes PhysicalProduct and DigitalProduct
    def update_stock(self, newquantity):
        self.stock = newquantity



    #Displays information about the physical product (Abstract Method from Product)
    def display_information(self):
        print(self._base_info() + f"Weight: {self.weight}" + f"\nProduct Type: Physical" + f"\n----------------------------\nSUPPLIER DETAILS: \n" +  f"Supplier ID: {self.suppid}" + f"\nName: {self.suppname}" + f"\nContact Info: {self.contact}\n----------------------------")

    #Prints fulfilment info for physical products (Abstract Method from Product)
    def get_fulfilment_info(self):
        return(f"This product requires physical shipping.")

    #Calculates Shipping Cost
    def calculate_shipping_cost(self):
        if self.weight > 200:
            shipping_cost = math.ceil(self.weight/200) * 3.50
        else:
            shipping_cost = 3.50
        return f"The shipping cost of {self.name} is ${shipping_cost:.2f}"

    #
    def to_dict(self):
        return{"id": self.itemid, "name": self.name, "price": self._price, "stock": self.stock, "weight": self.weight, "producttype": self.producttype, "supplierid":self.suppid, "suppliername": self.suppname, "contactinfo": self.contact}

    

