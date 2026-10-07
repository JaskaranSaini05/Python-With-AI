from  Session10 import Dish
from  Session10A import Menu
from  Session10B import Restaurant

dish1 = Dish()
dish2 = Dish(name='Paneer Tikka',price = 200 , rating = 4.5)
dish3 = Dish(name='Dal Makhani',price = 150 , rating = 4)
print('dish1',dish1)

print(dish1)
print(dish2)
print(dish3)

# List of Dishes
dishes = [dish1,dish2,dish3]
print(dishes)

menu = Menu(name="Indian Menu",
dishes = dishes,
number_of_Dishes = len(dishes))

print(menu)

restaurant = Restaurant(name='Johns Cafe',
phone='+9121222322',
email='johnscafe@gmail.com',
address='redwoord shores',
rating=4.5,
pricePerPerson=500,
menu=menu
)

restaurant.show()