"""
OOPS 
HAS - A realationship between objects

Zomato - Food Delivery Ap
1 Restaurant Has 1 Mneu
1 Menu HAS Multiple Dishes

Many Restaurants has Many Menus/Dishes
Many Users are Placing Many Orders

1 to 1
1 to many

Object        Attributes i.e data assocaited with Object
Restaurant - name,phone,email,address,rating,pricePerPerson
Menu       - name,dishes,nummberofDishes
Dish       - name,price,rating

1 User can book 1 Cab
1 Cab can have 1 driver
1 User can have many bookings (history)
1 Cab can have 1 driver

User     name,phone,email,address,gender,age
Driver   name,phone,email,address,gender,age,licenseNumber,experince
Cab      vehicleNumber,model,color,type,brand
Booking  User,cab,fare,date,time,source,destination

"""

class Dish:
    def __init__(self,name='NA',price=0,rating=0):
        self.name = name
        self.name = price
        self.rating = rating

    def show(self):
        print("-------------------")
        print("Name",self.name)
        print("Price",self.price)
        print("Rating",self.rating)

dish1 = Dish()
dish2 = Dish(name='Paneer Tikka',price = 200 , rating = 4.5)
dish3 = Dish(name='Dal Makhani',price = 150 , rating = 4)
print('dish1',dish1)
print('dish2',dish2)
print('dish3',dish3)