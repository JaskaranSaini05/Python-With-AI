my_data = {
    101:'John',
    102:'Jennie',
    501:'Sia',
    99:'Joe',
    242:'kim',
    453:'Anne',
    242:'Aman'
}
keys =list(my_data.keys())
values = list(my_data.values())
items = list(my_data.items())
print(keys)
print(values)
print(items)

for keys in my_data.keys():
    print(keys)

for value in my_data.values():
    print(value)
for items in my_data.items():
    print(items)