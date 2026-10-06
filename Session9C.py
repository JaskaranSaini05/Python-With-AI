
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
fionna = User()

# Reference Copy Operation
johnnie = john
mc_donalds = Restaurant()

print('john:',john,type(john),id(john))
print('johnnie:',johnnie,type(johnnie),id(johnnie))
print('mc_donalds:',mc_donalds,type(mc_donalds),id(mc_donalds))

# Wrtie Data in Object
john.name = 'John Watson'
john.phone = '+91 99999 88888'
john.email = 'John@example.com'
john.address = 'redwood shares'
john.gender = 'male'
john.age = 30

fionna.name = 'Fionna'
fionna.phone = '+91 99342 11111'
fionna.email = 'fionna@example.com'
fionna.address = 'country homes'
fionna.gender = 'female'
fionna.age = 28

print('data for john')
print(vars(john))

print('data for john')
print(vars(fionna))



