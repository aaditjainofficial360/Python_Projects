import Selling_food_inventory as food_inventory
recent_orders=[]

def place_orders(item,no_of_plates):
    # Placing Orders
    if len(recent_orders)<6:
        if item in food_inventory.food_inventory:
            food_inventory.food_order(item,no_of_plates)
            recent_orders.append(item)
        else:
            print('We cannot place your order. This item is out of stock..')
    else:
        print('We are busy at this moment!. Please wait...')

def last_recent_orders():
    print(f"Here are your last five orders : {recent_orders}")

Order1=place_orders('Dhokla',20)
#Order2=place_orders('Samosa',10)
#Order3=place_orders('Dahi Bhalla',7)
last_recent_orders()
