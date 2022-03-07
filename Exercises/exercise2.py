# This is my Application Overview for Exercise 2.

# 1, function simple(), write a function with 5 variables with messages attached and printed.

def simple():
    message1 = "Hello There,"
    message2 = "Welcome to my Function."
    message3 = "This is a Simple Function"
    message4 = "Composed of Several Messages"
    message5 = "Assigned to Variables and Printed."
    print(message1, message2, message3, message4, message5)


simple()


# 2, function simgple2(), write function with a message assigned to a variable and print it,
# then reassign the same variable to a different message after it is printed. Repeat until
# there are 4 different messages assigned to the same variable and 4 print functions accordingly.

def simple2():
    changing_message = "This function"
    print(changing_message)
    changing_message = "Uses the Same"
    print(changing_message)
    changing_message = "Variable to Print"
    print(changing_message)
    changing_message = "Several Messages."
    print(changing_message)


simple2()


# 3, function message(), write a function that takes one argument, write a print
# function that takes that argument.

def message(name):
    # Takes argument input into name parameter and inserts it into the print function.
    print(f"Welcome to {name.title()}'s program.")


message("Katlyn")
