# Restaurant to import
class Restaurant:

    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type

    def describe_restaurant(self):
        print(self.restaurant_name)
        print(self.cuisine_type)

    def open_restaurant(self):
        print("The restaurant is open")


class IceCreamStand(Restaurant):
    def __init__(self, restaurant_name, cuisine_type, flavors):
        super().__init__(restaurant_name, cuisine_type)
        self.flavors = list(flavors)

    def display_flavors(self):
        print(self.flavors)


stand1 = IceCreamStand("Teddy's", "Ice Cream", ("Chocolate", "Vanilla", "Strawberry"))
stand1.display_flavors()