# A shopkeeper has food items available with its quanitity(in pieces/plates)
food_inventory={'Samosa':500,'Jaleebi':200,'Bread Pakora':400,'Dhokla':700,'Gulab Jamun':600,'Emerti':700,
                'Aloo Puri':500,'Chole Bhature':900}
order_id=0
def food_order(item,no_of_pieces):
    if item in food_inventory:
        if food_inventory[item]>0:
            food_inventory[item]-=no_of_pieces
            global order_id
            order_id+=1
            print(f'Your Order is placed. Your Order Id is {order_id}')

        else:
            print('We are currently out of stock for this item.')

    else:
        print('We don\'t offer this item currently.')

O1=food_order('Idli Sambhar',6)
O2=food_order('Aloo Chat',5)
O3=food_order('Dhokla',20)
O4=food_order('Samosa',30)


