restaurant = {
    'name':"kylin experience",
    'description':'Asian,Chinese,Sushi,Thai',
    'address':'Chandigarh Phase 1 Industrial Area',
    'opearting_hours': '11 am - 11:30 pm',
    'prince for two': 1900,
    'phone number':'+95695695006',
    'menu': [
        {
            'name': 'vegetable  bowl',
            'price':750
        },
         {
            'name': 'Paneer Tikka',
            'price':450
        },
         {
            'name': 'vegetable noodles',
            'price':560
        }
    ]
}

print(restaurant)
print(restaurant['menu'])

# Converted the tuple to a list, changed an item, and converted it back to a tuple.
names = "Jaskaran","Aman"
name_list = list(names)
name_list[1] = "Gurpreet"
names = tuple(name_list)
print(names)