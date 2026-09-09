"""
def add(n1,n2,n3):
    result = n1 + n2 + n3
    print('result',result)
"""

# args: multiple arguements or variable arguments
# In python if you redefine a function,
# it overwrites old definition
# i.e. it will create a  new function
# *args -> receving input as tuple
def add(*args):
    print(args)
    print(type(args))
    print(id(args))
add(10,20,30)
add(10,20,30,40,50,60)
add(10,20,30,40,50,60,70,80)

def multiply(**kwargs):
    print(kwargs)
    print(type(kwargs))
    print(id(kwargs))

multiply(a=10,b=20,c=30)

def register_user(**user):
    print(user)

register_user(name='Jaskarn',email='jaskarnsingh@gmail.com',gender='male')

def fun(*args,**kwargs):
    print(args)
    print(kwargs)

fun(10,20,30,name='john',email='john@gmail.com')