# Explore Dicitionary Data Structure

# In Dicitionary kays are either number(int) or text(string)

# Dicitionary -> Keys cannot be duplicated. They are unique
#                but value can be duplicated
my_data = {
    101:'John',
    102:'Jennie',
    501:'Sia',
    99:'Joe',
    242:'kim',
    453:'Anne',
    242:'Aman'
}
"""
my_data = {
    'jo':'John',
    'je':'Jennie',
    'si':'Sia',
    'jj':'Joe',
    'ki':'kim',
    'an':'Anne',
    'am':'Aman'
}
"""
print('my_data')
print(my_data)


# Utility functions -> they work on keys
print('lenght',len(my_data))
print('minimum',min(my_data))
print('maximum',max(my_data))
print('sum',sum(my_data))

# Reading data from dicitionary
value = my_data[101]
print('value',value)

# update
my_data[101] ='Joseph'
print(my_data)

# delete
my_data.pop(101)
# del my_data[25]
print(my_data)

# add a new element
my_data[101] = 'Joseph'
print(my_data)