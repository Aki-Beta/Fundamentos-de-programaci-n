def show_menu ():
    print("\n" + "="*30)
    print("INVENTORY MANAGEMENT SYSTEM")
    print("="*30)
    print("1. Add product")
    print("2. Show inventory")
    print("3. Calculate statistics")
    print("4. Exit")
    print("—"*30)


def validate_number(massage, type = float):
    
    next = True
    while next:
        try:
            if type == "int":
                value = int(input(massage))
            else:  
                value = float(input(massage))
            return value
        except ValueError:
            print("Invalid input. Please enter a valid number.")

def add_product(inventory):

    product_name = input("\nEnter product name: ")
    product_price = validate_number("Enter product price: ", "float")
    product_quantity = validate_number("Enter product quantity: ", "int")

    # Cada producto es un diccionario dentro de la lista
    product = {
        "name": product_name,
        "price": product_price,
        "quantity": product_quantity
    }

    inventory.append(product)
    
    print("—"*30)
    print(f"Product '{product_name}' added successfully!")

def calculate_statistics(inventory):

    total_value = 0
    total_quantity = 0

    if not inventory:
        print("\nNo products to calculate")
        return
    for i, product in enumerate(inventory, 1):
        product_value = product["price"] * product["quantity"]
        total_value += product_value
        total_quantity += product["quantity"]
        print(f"{product['name']:} === ${product['price']:} === {product['quantity']:} === ${product_value:} ")
    
    print("—"*30)
    print(f"TOTAL ============== ${total_value:} ")
    


def main():
    inventory = [] 
    next_to = True

    while next_to:
        show_menu()
        choice = input("Choose an option: ")
        
        if choice == "1":
            add_product(inventory) 

        elif choice == "2":
            if not inventory:
                print("—"*30)    
                print("\nInventory is empty.")
            else:
                print("\n" + "—"*30)
                print("Product === Quantity === Price")
                print("—"*30)
                for product in inventory:
                    print(f" {product['name']} === {product['quantity']} === ${product['price']}")


        elif choice == "3":
            print("\nProduct === Quantity === Price")
            print("="*30)
            calculate_statistics(inventory)
            
            
        elif choice == "4":
            print("\n" + "—"*30)
            print("THANKS YOU FOR SHOPPING WITH US.")
            print("—"*30)
            break
        else:
            print("\nInvalid option. Please try again.")
            print("—"*30)
if __name__ == "__main__":
    main()