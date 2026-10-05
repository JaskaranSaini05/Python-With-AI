"""
Oops object oriented programming structure

1. In real world
 Object- Anything which exists is an object
         A real thing
         An entity
 Class - Drawing of an object
 
 Requirement:
 Mr.John is my client
 He wants to bild a cab booking solution

 In my application user should be able to login
 he can select a source and destination location
 he can view different cabs
 he can book a cab which allocates  him nearby driver
 he can pay online or in cash

 ..
 ...
 ....

 1.Identify the object i.e. Think of Object
 User - name ,phone,email,address,gender,age etc...
 Cabdriver - name,phone,email,address,gender,age,vehicleNumber,rating
 cab - vehiclenumber,color,model,type,companybrand etc..
 booking -  user,cab,cabdriver,date,time,fare,paymentMode etc etc..

1 user  can book many cabs
1 user at 1 time can have 1 booking
many users can book many cabs

"""
class Cab:
    # In python,__init__ is constructor and it remains in all the classes in python

    def __init__(self):
        print('constructor executed')
        print('self:',self,type(self),id(self))

john_cabs = Cab()
print('john_cabs:',john_cabs,type(john_cabs),id(john_cabs))