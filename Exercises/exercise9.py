# Exercise 9 Classes and Functions

# Write functions for each and then call the function to ensure results are correct.

# 1) Do 8-3 through 8-5

# 8 - 3 T-Shirt
# Write a function called make_shirt() that accepts a size and the text of a message
# that should be printed on the shirt, the function should then print a sentence
# summarizing the size and messages printed on the shirt. Call it once with positional
# arguments and a second time with keyword arguments.
def make_shirt(size, message):
    print(f'The shirt is size {size} and will have "{message}" printed on it.')


make_shirt(6, "Happy Birthday")
make_shirt(size=2, message="Enjoy yourself")


# 8 - 4 Large Shirts
# Modify the make_shirt() function so the shirts are large by default with a message
# that reads "I love Python." Make a large shirt and a medium shirt with the default
# message and a shirt of any size with a different message on it.
# I simply repeated the code below, while keeping it above as it was.
def make_shirt(size='Large', message='I love Python.'):
    print(f'The shirt is size {size} and will have "{message}" printed on it.')


make_shirt()
make_shirt(size='Medium')
make_shirt(size='Small', message="Potatoes Rock")


# 8 - 5 Cities
# Write a function called describe_city() that accepts the name of a city and
# its country. It should print a simple sentence like "city is in country". Give
# the parameter for the country a default value. Call the function for 3 different
# cities, at least one not in the default country.
def describe_city(city, country="The United States of America"):
    print(f"{city} is in {country}")


describe_city("Wichita")
describe_city("Dublin", "Ireland")
describe_city("New York")


# 2) Do 8-9 through 8-11

# 8 - 9 Messages
# Make a list containing a series of short text messages. Pass the list
# to a function called show_messages() which prints each text message.
text_messages = ["Hello there.", "How are you?", "Nice to see you."]


def show_messages(messages):
    for text in messages:
        print(text)


show_messages(text_messages)


# 8 - 10 Sending Messages
# Start with a copy of the program from 8-9. write a function send_message()
# that prints each text message and moves each message to a new list called
# sent_messages() as it's printed. After calling the function, print both lists
# to make sure the messages moved correctly.
text_messages = ["Hello there.", "How are you?", "Nice to see you."]
sent_messages = []


def send_messages(messages):
    while messages:
        current_message = messages.pop()
        print(current_message)
        sent_messages.append(current_message)


send_messages(text_messages)
print(text_messages)
print(sent_messages)


# 8 - 11 Archived Messages
# Start with work from 8-10. Call the function send_message() with a copy
# of the list of messages. After calling, print both lists to show that
# the original list has retained its messages.
text_messages = ["Hello there.", "How are you?", "Nice to see you."]
sent_messages = []


def send_messages(messages):
    while messages:
        current_message = messages.pop()
        print(current_message)
        sent_messages.append(current_message)


send_messages(text_messages[:])
print(text_messages)
print(sent_messages)


# 3) Do 9-1 through 9-3

# 9 - 1 Restaurant
# Make a class called Restaurant. The __init__() method for Restaurant
# should store 2 arguments, a restaurant_name and a cuisine_type. Make a
# method called describe_restaurant() that prints those two pieces of information
# and a method called open_restaurant() hat prints a message indicating
# the restaurant is open. Make an instance called restaurant from the class.
# print the two attributes individually, and then call both methods.
class Restaurant:

    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type

    def describe_restaurant(self):
        print(self.restaurant_name)
        print(self.cuisine_type)

    def open_restaurant(self):
        print("The restaurant is open")


restaurant = Restaurant("Great Buffet", "Chinese")
print(restaurant.restaurant_name)
print(restaurant.cuisine_type)
restaurant.describe_restaurant()
restaurant.open_restaurant()


# 9 - 2 Three Restaurants
# Start with class from 9-1. Create three different instances
# from the class, and call describe_restaurant() for each.
# This time, as there are no changes to the class, I am only going to
# fill out the details from this portion.
restaurant1 = Restaurant("McDonald's", "Fast Food")
restaurant1.describe_restaurant()
restaurant2 = Restaurant("Carlos O' Kelly's ", "Mexican")
restaurant2.describe_restaurant()
restaurant3 = Restaurant("Taco Bell", "Fast Food")
restaurant3.describe_restaurant()


# 9 - 3 Users
# Make a class called User. Create two attributes called first_name
# and last_name, and then create several other attributes typically
# stored in a user profile. Make a method called describe_user()
# that prints a summary of the user's information. Make another method
# called greet_user() that prints a personalized greeting to the user.
# Create several instances for different users and call both methods for each user.
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


user1 = User("Iris", "Frank", "FlowerGirl", "Female")
user1.describe_user()
user1.greet_user()
user2 = User("Ryou", "Ryudo", "DragonKid", "Male")
user2.describe_user()
user2.greet_user()
user3 = User("Rosalie", "Lackey", "PotatoLord", "female")
user3.describe_user()
user3.greet_user()


# 4) Do 9-4 and 9-5

# 9 - 4 Number Served
# Start with exercise 9-1 and add an attribute called number_served
# with a default of 0. Create an instance called restaurant from this class
# Print the number of customers the restaurant has served, and then change
# this value and then change this value and print it again. add a method called
# set_number_served() that lets you set the number of customers served Call this
# method with a new number and print this method again. Add a method called
# increment_number_served() that lets you increment the number of customers served.
# Call this with any number you like that could represent customers served in, say, a day.
class Restaurant:

    def __init__(self, restaurant_name, cuisine_type, number_served=0):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        self.number_served = number_served

    def describe_restaurant(self):
        print(self.restaurant_name)
        print(self.cuisine_type)

    def open_restaurant(self):
        print("The restaurant is open")

    def set_number_served(self, number):
        self.number_served = number

    def increment_number_served(self, served):
        self.number_served += served


restaurant = Restaurant("Burger King", "Fast Food")
# I called the describe_restaurant method because I wanted the labeling
restaurant.describe_restaurant()
print(restaurant.number_served)
restaurant.number_served = 50
print(restaurant.number_served)
restaurant.set_number_served(40)
print(restaurant.number_served)
restaurant.increment_number_served(50)
# Comment Below is to check the increment.
# print(restaurant.number_served)


# 9 - 5 Login Attempts:
# Add an attribute called login_attempts to user class from 9-3.
# Write a method called increment_login_attempts() that increments
# the value of login attempts by 1. Write another method called
# reset_login_attempts() that resets the value of login_attempts to 0.
# Make an instance of the User class and call increment_login_attempts()
# several times. Print the value of login_attempts to make sure it was
# incremented properly, and then call reset_login_attempts(). Print
# login_attempts again to make sure it was reset to 0.
class User:
    def __init__(self, first_name, last_name, username, gender, login_attempts=0):
        self.first_name = first_name
        self.last_name = last_name
        self.username = username
        self.gender = gender
        self.login_attempts = login_attempts

    def describe_user(self):
        print(self.username)
        print(self.first_name)
        print(self.last_name)
        print(self.gender)

    def greet_user(self):
        print(f"Welcome, {self.first_name} {self.last_name}.")

    def increment_login_attempts(self):
        self.login_attempts += 1

    def reset_login_attempts(self):
        self.login_attempts = 0


user4 = User("Jane", "Doe", "PowerPuff", "female")
# printed describe_user, so I could have some description and separation.
print(user4.describe_user())
user4.increment_login_attempts()
user4.increment_login_attempts()
print(user4.login_attempts)
user4.reset_login_attempts()
print(user4.login_attempts)
