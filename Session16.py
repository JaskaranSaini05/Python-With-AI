"""

Single Value Containers(which can hold only 1 value)
int,float,bool

Multi Value Contaiers(which can hold lot of data)
objects - tuple,list,string,set,dictionary

Sequence or linear
   tuple
   list
   strings

  Storage of the data is non sequential or nonlinear
  set
  dictionary

Properties
1.Indexing
2.Negative Indexing
3.Slicing
4.Concatenation
5.Multiplicty
6.Membership Testing
"""

# List
my_data = [10,20,30]
print('my_Data[0]',my_data[-1])
print('lenght of my_Data',len(my_data))

# List of Lists

numbers = [
#0  1  2    
[10,20,30],  #0
[40,50,60],  #1
[70,80,90],  #2

]

print('numbers[0]',numbers[0])
print('length of numbers',len(numbers))
print('numbers[-1]',numbers[-1])
print('numbers[0][2]',numbers[0][2])

# LIST OF LIST OF LISTS
# 3-D List
large_Data = [
    [
        #0  1  2    
[10,20,30],  #0
[40,50,60],  #1
[70,80,90],  #2

    ],
     [
        #0  1  2    
[10,20,30],  #0
[40,50,60],  #1
[70,80,90],  #2

    ],


]

print('large_Data[1][2][1]',large_Data[1][2][1])
print('large_Data[-1][-3][-2]',large_Data[-1][-3][-2])

name ="Johns Cafe"
message = """
This is awesome 
welcome to johns cafe
you get happiness  with
   good food
"""
print('message')
print(message)

print('--------------------------')
#3. Slicing

data = list(range(10,101,10))
print('data:',data)
print(data[0:3])# pickup elements starting from 0 till 2 i.e. less than 3
print(data[3:7]) 
print(data[5:])
print(data[ : -5])

email ='john@example.com'
print('name =', email[0:4])
print('domain =', email[5:])


# Concatenation
# combine elements of data1 and data2 to create a new list data 3
data1 = [10,20,30]
data2 = [40,50,60]

data3 = data1 + data2
print('data3',data3)

data1 = (10,20,30)
data2 = (40,50,60)
data3 = data1 + data2
print('data3',data3)

string1 = "jaskarn"
string2 = "singh"

string3 = string1 + string2
print('string3',string3)

#5. Multiplicity
data4 = data1 * 3
print('data4',data4)

#6. Membership Testing

print('10 in data1',10 in data1)
print("exam in email",'exam' in email)
print("hello not in email",'hello' not in email)