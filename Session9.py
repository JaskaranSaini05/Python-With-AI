"""
Oops object oriented programming structure

1. In real world
 Object- Anything which exists is an object
         A real thing
         An entity
 Class - Drawing of an object
 
 Requirement:
 Mr.John is my client
 He is running a restaurant
 He wants to bild an online food delivery system

 In my application user should be able to login
 he can select a restaurant
 he can view its menu
 Add dishes to cart and then place an order

 ..
 ...
 ....

 1.Identify the object i.e. Think of Object
 User - name ,phone,email,address,gender,age etc...
 DeliveryAgent - name,phone,email,address,gender,age,vehicleNumber,rating
 Restaurant - name,phone,email,address,operatinghours,pricePerPerson
 Menu - dishes,category,totalDishes etc...
 Dish - name,image,price,rating etc..
 Order - dishes,user,deliveryAddress,restaurant,deliveryAgent
 
 1 User can place many orders
 1 restaurant can have many dishes
 many users can place many orders..

 etc etc etc
 
"""
# 2.Create Class for the Object
# User - name,phone,email,address,genderage
# Restaurant - name,phone,email,address,operatinghours,pricePerPerson

class User:
    # In python,__init__ is constructor and it remains in all the classes in python
    # self is an input to __init__ (i.e an argument)
    # Use Proper Indenetation(tab space after:)
    def __init__(self):
        print('constructor executed')
        print('self:',self,type(self),id(self))

class Restaurant:
    # In python,__init__ is constructor and it remains in all the classes in python

    def __init__(self):
        print('constructor executed')
        print('self:',self,type(self),id(self))

# 3. Create Objects in Memory Using Class
# Object Construction Statement
# LHS: john is a reference variable,it will hold the hashcode of object in RAM
# RHS: User() s creation of an object ,which automatically executes __init__(constructor)
john = User()
mc_donalds = Restaurant()

print('john:',john,type(john),id(john))
print('mc_donalds:',mc_donalds,type(mc_donalds),id(mc_donalds))