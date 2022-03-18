# Exercise 13 Modules and PiP

# Write a function for each and then call to verify

# 1) Do 8-15 through 8-17

# 8 - 15 Printing Models
# Put the functions for the example printing_models.py in a separate file called
# printing_functions.py and modify the file to use the imported functions.
import printing_function
def printing():
    printing_function.testing_functions()


printing()


# 8 - 16 Imports
# Using a program you wrote with one function in it, store that function in a separate
# file. Import the file into the main program file and call it using different approaches.
def importing_items():
    import printing_function
    from printing_function import testing_functions
    from printing_function import testing_functions as tn
    import printing_function as pf
    from printing_function import *


importing_items()

# 8 - 17 Styling Functions
# Choose any of the 3 program written for the chapter and make sure they follow the
# guidelines detailed in this section.
# If we simply use the very basic one of printing_function, it is so simple, it
# already follows the guidelines.

# 2) Do 9-10 through 9-12

# 9 - 10 Imported Restaurant
# Using latest Restaurant class, store it in a module. Make a separate file that
# imports Restaurant. Make a Restaurant instance, and call one of Restaurant's methods to
# show the import statement is working properly.
import Restaurant


def import_rest():
    restaurant1 = Restaurant.Restaurant("Taco Bell", "Fast Food")
    restaurant1.describe_restaurant()


import_rest()


# 9 - 11 Imported Admin
# Start with work from 9-8. Store classes User, Privileges, and Admin in one module.
# Create a separate file, make an Admin instance and call show_privileges() to show
# that everything is working.
import usernamesfile


def import_admin():
    admin1 = usernamesfile.Admin("John", "Snow", "God of War", "Male", usernamesfile.privileges2)
    usernamesfile.privileges2.show_privileges()


import_admin()


# 9 - 12 Multiple Modules
# Store the User class in one module, abd store the Privileges and Admin classes
# in a separate module. In a separate file, create an Admin instance and call
# show_privileges() to show that it all works.
# I couldn't think of anything else to label them.
import UserOnly
import usernamedetailsminususer


def multi_mod():
    usernamedetailsminususer.Admin("John", "Doe", "Mystery", "Male", usernamedetailsminususer.privileges2)
    usernamedetailsminususer.privileges2.show_privileges()


multi_mod()


# 3) 9 - 16 Python Module of the Week
# One excellent resource for exploring the Python standard library is a site called
# Python Module of the Week. Go there and look at the table of content. Find a module
# that looks interesting to you and read about it.

# In general, I find the random module one of the more interesting ones since it gives
# so many varieties of answers, while making many different ways to use it.
