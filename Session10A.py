class Menu:

    def __init__(self,name='NA',dishes=[],number_of_Dishes=0):
        self.name = name
        self.dishes= dishes
        self.number_of_Dishes = number_of_Dishes

    def show(self):
        print('------------')
        print("Name",self.name)
        print("Dishes",self.dishes)
        print("Number_of_Dishes",self.number_of_Dishes)
"""
menu = Menu()
print('menu:',menu)
menu.show()
"""