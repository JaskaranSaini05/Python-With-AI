class Restaurant:
    def __init__(self,name='NA',phone='NA',email='NA',
    address='NA',rating=0,pricePerPerson=0,menu=None):

        self.name = name
        self.phone = phone
        self.email = email
        self.address = address
        self.rating = rating
        self.pricePerPerson = pricePerPerson
        self.menu = menu

    def show(self):
        print("-------------------")
        print('Name',self.name)
        print('Phone',self.phone)
        print('Email',self.email)
        print('Address',self.address)
        print('Rating',self.rating)
        print('Price_per_person',self.pricePerPerson)
        print('Menu',self.menu)
        print("-------------------")

