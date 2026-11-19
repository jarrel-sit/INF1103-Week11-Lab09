#Creating Supplier(Blueprint)
class Supplier:
    def __init__(self, supplier_id:str, supplier_name:str, contact_email:str):
        self.supplier_id = supplier_id
        self.supplier_name = supplier_name
        self.contact_email = contact_email