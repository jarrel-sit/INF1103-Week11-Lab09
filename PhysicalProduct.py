from Product import Product, CanBeShipped
from Supplier import Supplier

#Physical Product Class
class PhysicalProduct(Product, CanBeShipped):
    def __init__(self, name: str, itemid: str, price: float, stock: int, supplier: Supplier, weight: float, producttype: str):
        super().__init__(name,itemid,price,stock,supplier)
        self.suppid = supplier.supplier_id
        self.suppname = supplier.supplier_name
        self.contact = supplier.contact_email
        self.weight = weight
        self.producttype = producttype