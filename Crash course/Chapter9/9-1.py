class Restaurant:
    """A simple restaurant class"""

    def __init__(self, name, cuisine):
        """initialize name and cuisine attributes"""
        self.name = name
        self.cuisine = cuisine

    def describe_restaurant(self):
        print(f"The name of the restaurant {self.name.title()}")
        print(f"The restaurant serves {self.cuisine.title()}")

    def open_restaurant(self):
        print(f"{self.name} is now open.")


rest = Restaurant('Corner', 'patat')
chines = Restaurant('Great wall', 'chinese')
mac = Restaurant('Mac Donalds', 'fast food')
rest.describe_restaurant()
rest.open_restaurant()

chines.describe_restaurant()
mac.describe_restaurant()



