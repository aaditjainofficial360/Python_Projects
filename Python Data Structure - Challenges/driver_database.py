driver_details=[]


def feed_driver_details(driver_name,car_type,capacity):
    driver_details.append((driver_name,car_type,capacity))
    print('Database Updated!')

def driver_info():
    print('Here are the driver details :')
    for row in driver_details:
        print(row)

D1=feed_driver_details('Rajan','Sedan',4)
D2=feed_driver_details('Sonu','hatchback',4)
D3=feed_driver_details('Ravi','Hatchback',6)
D4=feed_driver_details('Arjun','SUV',8)
driver_info()