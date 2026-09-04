# Loops
# Indexing
#       0   1  2 3  4
data = [10,20,30,40,50]
print(data,type(data),id(data))

print(data[0])
print(data[-1])

for index in range(0,5,1):
    print(data[index])

# Enhanced for loop or for each loop 
# -> This works with indexed data strucutres in python
# as well non indexed data structres
# this is read only loop
for number in data:
    print(number)