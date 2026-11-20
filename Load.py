from Inventory import Inventory
from Supplier import Supplier
from Product import Product
from ProductFactory import ProductFactory
import csv

class Load:
    def load_products(self, path: str, inventory: Inventory, supplier: Supplier) -> None:
        self.inventory = inventory
        self.supplier = supplier

        try:
            file = open(path, newline="")
        except FileNotFoundError:
            print(f"Products file not found: {path}")
        else:
            with file:
                reader = csv.reader(file)
                next(file, None)
                loaded = 0
                for line_number, row in enumerate(reader, start=2):
                    try:
                        product_type, product_id, name, price, stock, extra = row
                        product = ProductFactory.create(
                            product_type.strip().lower(),
                            product_id,
                            name,
                            float(price),
                            int(stock),
                            supplier,
                            extra
                        )
                        inventory.add_product(product)   # use your Inventory's method name
                    except ValueError as e:
                        print(f"Skipping row {line_number}: {e}")
                    else:
                        loaded += 1
            print(f"{loaded} products loaded.")
        finally:
            print("Load attempt finished.")

load = Load()
inventory = Inventory()
supplier1 = Supplier("S1", "Jarrel", "jarrel@gmail.com")
load.load_products("products.csv", inventory, supplier1)

#I added an additional parameter for the weight/download size, if not none of the products would even be created
