
store_dict = {}
to_execute = True

def start():
    while to_execute:
        print('''
        1.Add products.
        2.Update stock.
        3.Sell product.
        4.Display inventory.
        5.Display most-expensive product.
        6.Total_potential sales.
        7.Exit
        ''')
        user_choice = int(input("Enter your choice: "))
 
        implementation(user_choice)

def implementation(user_choice):
    if user_choice == 1:

        name = input("Enter the product name: ")
        price = float(input("Enter price: "))
        quantity = int(input("Quantity: "))
        add_product(store_dict,name,price,quantity)

    elif user_choice == 2:
        name = input("Enter product name to update: ")
        quantity = int(input("Enter the quantity to be updated: "))
        update_stock(store_dict,name,quantity)

    elif user_choice == 3:
        name = input("Enter name of product to sell: ")
        quantity = int(input("Enter the quantity of product to sell: "))
        sell_product(store_dict,name,quantity)

    elif user_choice == 4:
        display_inventory(store_dict)

    elif user_choice == 5 :
        most_expensive_product(store_dict)

    elif user_choice == 6:
        print("the total potential sale is :",total_potential_sale(store_dict))

    elif user_choice == 7:
        terminate()
     
    else:
        return "Invalid option"

def add_product(store_dict,name,price,quantity):
    if name  not in store_dict:
        store_dict[name] ={"price":price,"quantity":quantity}
        print(f"{name} succesfully addeda")
        print(store_dict)
        return 1
    else:
        print(f"{name} already exist")
        return 1

def update_stock(store_dict,name,quantity):
    if name in store_dict:
        store_dict[name]["quantity"] += quantity
        print(f"The updated version is: {store_dict}")
    else:
        print(f"{name} does not exist!")

def sell_product(store_dict,name,quantity):
    if name in store_dict:
        if len(store_dict[name]) != 0 and quantity <= store_dict[name]["quantity"]:
            store_dict[name]["quantity"] -= quantity
            print(store_dict)
            result = store_dict[name]["price"] * quantity
            print(f"the price of {name} is : {result}")
        else:
            print(f"{name} is out of stock")
    else:
        print("such product does not exist")    

def display_inventory(store_dict):
    for key,value in store_dict.items():
        print(f"name :{key}: price:{value["price"]},quantity:{value["quantity"]}")
    length = len(store_dict.keys())
    return length

def most_expensive_product(store_dict):
    expensive = 0
    if len(store_dict) != 0:
        for key,value in store_dict.items():
            if value["price"] > expensive:
                expensive = value["price"]
                product_name = key
        print(f"the most expensive product in the dictionary is: {product_name} with: {expensive}")
    else:
        print("No product is available")

def total_potential_sale(store_dict):
    if len(store_dict) != 0:
        for value in store_dict.values():
            total_sale =  (value["price"] * value["quantity"])
  
            return total_sale
    else:
        print("No products available!")

def terminate():
    global to_execute
    to_execute = False
    print("Goodbye")
    
start()
