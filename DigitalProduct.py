from Product import Product
from Supplier import Supplier

#DigitalProduct Class      
class DigitalProduct(Product):
    def __init__(self, name: str, itemid: str, price: float, stock: int, supplier: Supplier, download_size: float, producttype: str):
        super().__init__(name,itemid,price,stock, supplier)
        self.download_size = download_size
        self.producttype = producttype
        self.suppid = supplier.supplier_id
        self.suppname = supplier.supplier_name
        self.contact = supplier.contact_email

    #Displays information about the digital product (Abstract Method from Product)
    def display_information(self):
        print(self._base_info() + f"Download Size: {self.download_size}\n"f"Product Type: Digital" + f"\n----------------------------\nSUPPLIER DETAILS: \n" +  f"Supplier ID: {self.suppid}" + f"\nName: {self.suppname}" + f"\nContact Info: {self.contact}\n----------------------------")

    #Prints fulfilment info for digital products (Abstract Method from Product)
    def get_fulfilment_info(self):
            return(f"This product will be delivered digitally.")

    #Converts Digital Product Object into JSON-readable data (Abstract Method from Product)
    def to_dict(self):
        return{"id": self.itemid, "name": self.name, "price": self._price, "stock": self.stock, "downloadsize": self.download_size, "producttype": self.producttype, "supplierid":self.suppid, "suppliername": self.suppname, "contactinfo": self.contact}