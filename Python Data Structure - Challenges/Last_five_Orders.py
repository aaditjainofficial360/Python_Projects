
recent_orders=[]

def place_orders(item):
    # Placing Orders
    recent_orders.append(item)

def last_recent_orders():
    print(f"Here are your last five orders : {recent_orders[:5]}")

Order1=place_orders('Dhokla')
Order2=place_orders('Samosa')
Order3=place_orders('Dahi Bhalla')
Order4=place_orders('Aloo Tikki')
Order5=place_orders('Pav Bhaji')
Order6=place_orders('Jaleebi')
last_recent_orders()
