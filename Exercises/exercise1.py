print('Hello World')
# Make a typo somewhere in that line and then run the program again.
# Added a p onto print
# Can you make a typo that generates an error?
# Prior typo generated an error as printp is not an established function.
# Can you make a typo that doesn't generate an error?
# Formed typo by adding in an additional h to hello
# Why do you think it didn't generate an error?
# It didn't generate an error because the typo is in the string
# as a result, while the program counts it as a typo, since it does not
# affect the ability for the program to run, it does not make an error.


# The import this, once plugged into the Python Console
# brings up The Zen of Python by Tim Peters.
# This output describes the priority line for code development to better readability.
# Overall this output emphasizes that the best way to code is the simplest way that
# runs properly and focuses on readability. That being said, although it is best
# to code a working code over a perfect code, it should not be coded without thought
# of how to implementation of the code can be understood.


# Assign a message to a variable and then print that message.
a = 'Welcome'
# Assigned the message 'Welcome' to the variable 'a'.
print(a)
# Printed the variable 'a', which printed the message associated with the variable.


# Assign a message to a variable, print that message, change the value to a new message
# and then print the new message.
b = 'Every day counts'
# Assigned the message 'Every day counts' to variable 'b'.
print(b)
# Printed variable 'b', which printed the associated message.
b = 'Live like it'
# Assigned new message 'Live like it' to variable 'b'.
print(b)
# Printed variable 'b' which printed the new message.


# Write a function called display_message() that prints one sentence telling everyone what
# you are learning about in this chapter. Call the function and make sure the message
# displays correctly.
def display_message():
    # Defines/creates function display_message
    print('In this chapter we are learning about defining and calling a function.')
    # prints message once function is called


display_message()
# Calls the function

# Write a function called favorite_book() that accepts one parameter, title. This function
# should print a message, such as 'One of my favorite books is Alice in Wonderland'.
# Call the function, making sure to include a book title as an argument in the function call.


def favorite_book(title):
    # Creates function favorite_book with parameter title.
    print(f"One of my favorite books is {title}.")
    # Printed function message with parameter, title being called.


favorite_book('The Gift of Dragons')
# Calls function with inserted argument, 'The Gift of Dragons'.
