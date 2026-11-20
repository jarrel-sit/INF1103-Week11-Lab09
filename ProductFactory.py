from PhysicalProduct import PhysicalProduct
from DigitalProduct import DigitalProduct
from Supplier import Supplier
from Product import Product

class ProductFactory:
 @staticmethod
 def create(product_type: str, product_id: str, name: str, price: float,
    stock_quantity: int, supplier: Supplier, extra: float) -> Product:
    if product_type == "physical":
        
        return PhysicalProduct(product_id, name, price, stock_quantity, supplier, extra, product_type)
    elif product_type == "digital":
        return DigitalProduct(product_id, name, price, stock_quantity, supplier, extra, product_type)
    # else:
    #     raise ValueError(f"Unknown product type: {product_type}")