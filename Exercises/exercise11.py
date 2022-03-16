# Exercise 11 Inheritance and Polymorphism

# For 1 through 3, write as functions and call them to check.

# 1) 9 - 6 Ice Cream Stand
# Write a class called IceCreamStand that inherits from the Restaurant class
# you wrote in either 9-1 or 9-4. Add an attribute called flavors that stores a
# list of ice cream flavors. Write a method that displays these flavors.
# Create an instance of IceCreamStand and call this method.
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


# 2) 9 - 7 Admin
# Write a class called Admin that inherits from the User class from 9-3 or 9-5.
# Add an attribute, privileges, that stores a list of strings like "can add post",
# "can delete post", "can ban user" and so on. Write a method called show_privileges()
# that lists the administrator's set of privileges. Create an instance of Admin and call this method.
class User:
    def __init__(self, first_name, last_name, username, gender):
        self.first_name = first_name
        self.last_name = last_name
        self.username = username
        self.gender = gender

    def describe_user(self):
        print(self.username)
        print(self.first_name)
        print(self.last_name)
        print(self.gender)

    def greet_user(self):
        print(f"Welcome, {self.first_name} {self.last_name}.")


class Admin(User):
    def __init__(self, first_name, last_name, username, gender, privileges):
        super().__init__(first_name, last_name, username, gender)
        self.privileges = list(privileges)

    def show_privileges(self):
        print(self.privileges)


admin1 = Admin("John", "Doe", "AdminUser", "Male", ("can add post", "can delete post",
                                                    "can ban user", "can unban user"))
admin1.show_privileges()


# 3 9 - 8 Privileges
# Write a separate Privileges class with one attribute, privileges, that stores a list of
# strings described in 9-7. Move the show_privileges() method to this class. Make a
# Privileges instance as an attribute in Admin class. Create new Admin instance and use
# method to show its privileges.
class Privileges:
    def __init__(self, privileges):
        self.privileges = list(privileges)

    def show_privileges(self):
        print(self.privileges)


# By copying the Admin class, it allows for the usage of an instance as an attribute
class Admin(User):
    def __init__(self, first_name, last_name, username, gender, privileges):
        super().__init__(first_name, last_name, username, gender)
        self.privileges = privileges2


privileges2 = Privileges(("can ban user", "can unban user", "can remove post"))
admin2 = Admin("Jane", "Matthews", "DoeEyed", "Female", privileges2)
privileges2.show_privileges()
