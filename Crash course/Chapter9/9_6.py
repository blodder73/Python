class Restaurant:
    """A simple restaurant class"""

    def __init__(self, name, cuisine):
        """initialize name and cuisine attributes"""
        self.name = name
        self.cuisine = cuisine
        self.number_served = 0

    def describe_restaurant(self):
        print(f"The name of the restaurant {self.name.title()}")
        print(f"The restaurant serves {self.cuisine.title()}")

    def open_restaurant(self):
        print(f"{self.name} is now open.")

    def read_number_served(self):
        print(f"This restaurant served {self.number_served} customers.")

    def set_number_served(self, init_customer):
        self.number_served = init_customer

    def incr_number_served(self, customer):
        self.number_served += customer


class IceCreamStand(Restaurant):

    def __init__(self, name, cuisine):
        super().__init__(name, cuisine)
        self.flavors = ['vanilla', 'chocolate', 'pistache']


rest = Restaurant('Corner', 'patat')
chines = Restaurant('Great wall', 'chinese')
mac = Restaurant('Mac Donalds', 'fast food')
rest.describe_restaurant()
rest.open_restaurant()

chines.describe_restaurant()
mac.describe_restaurant()

print(f"Start number served in restaurant {rest.name} = {rest.number_served}")
rest.set_number_served(50)
print(f"Initialized number served in restaurant {rest.name} = {rest.number_served}")
rest.incr_number_served(25)
print(f"Incremented number with 25 served in restaurant {rest.name} = {rest.number_served}")

ice = IceCreamStand('happy ice', 'icecream')
ice.describe_restaurant()
print(f"We have flavors: {ice.flavors[0]}, {ice.flavors[1]}, {ice.flavors[2]}")



