# Create Statement
num1= 10
num2= 20
# num1 is a refernce variable created in stack of ram
# 10 gets stored in a container of tpye int in heap of ram
result= num1 + num2

# Read Statement
print(result)
print('num1 is', num1)
print('num hashcode now is',id(num1))
print('type of numm1 is',type(num1))

# Update Statement
num1 = 20
print('num1 is', num1)
print('num hashcode now is',id(num1))
print('type of numm1 is',type(num1))

# Delete Statement
# Explicit (del statement) or Implicit (Automatic)
del num1
print('num1 is', num1)
print('num hashcode now is',id(num1))
print('type of numm1 is',type(num1))