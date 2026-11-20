#Importing of classes from other files
from Supplier import Supplier
from Inventory import Inventory
from ProductFactory import ProductFactory
from Validation import Validation

#Menu Display and User Input    
def menu():
    while True:
        print('\n\tMenu\n=======================\n1. Display all products\n2. Add a product\n3. Remove Product\n4. Update Stock\n5. Search for a product\n6. Save Inventory\n7. Exit')
        option = input('> ')
        match(option):
            #Runs display inventory method
            case "1":
                if not inventory:
                    print('Inventory is empty!')
                else:
                    inventory.display_all()

            #Runs add product method
            case "2":
                while True:
                    try:
                        itemid = input('ID: ')
                        name = input('Name of Product: ')
                        price = Validation.get_positive_float("Price of Product: ")
                        stock = int(input('Stock: '))
                        if stock <= 0:
                            raise ValueError("Stock must be greater than 0")
                        producttype = str(input("Physical or Digital? ")).lower()
                        if producttype == "physical":
                            extra = Validation.get_positive_float("Input Weight of Product: ")
                        elif producttype == "digital":
                            extra = Validation.get_positive_float("Input Download Size of Product: ")
                        else:
                            raise ValueError("Unknown product type")
                        inventory.add_product(ProductFactory._create(producttype, itemid, name, price, stock, supplier1, extra))
                        print('Product created')
                        break
                    except ValueError:
                        print("Invalid format, please key in again")

            #Runs remove product method              
            case "3":
                itemid = input('ID: ')
                inventory.remove_product(itemid)
                    
            #Runs update stock method
            case "4":
                updateid = input("\nPlease enter the Product ID of the product that you want to update the stock for.\n")
                newquantity = int(input("Please enter the new quantity of the product you want to update the stock for."))
                inventory.update_product_stock(updateid, newquantity)
            #Runs search by ID method 
            case "5":
                searchid = input("\nPlease enter the Product ID of the product you are looking for.\n")
                inventory.find_product(searchid)
            #Saving inventory to json
            case "6":
                inventory.save_inventory()
            #Save to JSON and exit
            case "7":
                inventory.save_inventory()
                break
            #Handles invalid inputs
            case _:
                print('Invalid Response, please input a value 1-7.')
            

#Loads inventory and menu if file is run
if __name__ == "__main__":
    supplier1 = Supplier("S1", "Jarrel", "jarrel@gmail.com")
    inventory = Inventory()
    inventory.load_inventory()
    menu()
