# Exercise 6 Control Flow

# 1) 5 - 3 Alien Colors #1
# Imagine an alien was shot down in a game. Create a variable called
# alien_color and assign it a value of 'green', 'yellow', or 'red'.
# Write an if statement to test if the alien's color is green, if so print
# a message that the player just earned 5 points.
# Write one version of the program that passes the if test and another that fails
# Note: the one that fails will have no output.

# Passes 5 - 3 if statement
alien_color = "green"
if alien_color == "green":
    print("You earned 5 points.")
# Fails the if statement
alien_color = "red"
if alien_color == "green":
    print("You earned 5 points.")


# 2) 5 - 4 Alien Colors #2
# Choose a color for the alien like above, and write an if-else chain.
# If alien color is green, earned 5 points. Otherwise, earned 10 points.
# Write one version that runs the if block and one that runs the else block.

# Runs the if block
alien_color = "green"
if alien_color == "green":
    print("You earned 5 points.")
else:
    print("You earned 10 points")
# Runs the else block
alien_color = "yellow"
if alien_color == "green":
    print("You earned 5 points.")
else:
    print("You earned 10 points.")


# 3) 5 - 5 Alien Colors #3
# Turn your if-else chain from above into an if-elif-else chain.
# If alien is green, print player earned 5 points, if alien is yellow,
# print player earned 10 points, if alien was red, print player earned 25 points.
# Write 3 versions, making sure each message is printed for the appropriate color alien.

# Green Alien
alien_color = "green"
if alien_color == "green":
    print("You earned 5 points.")
elif alien_color == "yellow":
    print("You earned 10 points.")
else:
    print("You earned 15 points.")
# Yellow Alien
alien_color = "yellow"
if alien_color == "green":
    print("You earned 5 points.")
elif alien_color == "yellow":
    print("You earned 10 points.")
else:
    print("You earned 15 points.")
# Red Alien
alien_color = "red"
if alien_color == "green":
    print("You earned 5 points.")
elif alien_color == "yellow":
    print("You earned 10 points.")
else:
    print("You earned 15 points.")


# 4) 5 - 6 States of Life
# Write an if-elif-else chain that determines a person's stage of life.
# set a value for the variable age and then; if less tha 2 years print person
# is a baby, if at least 2 years but less than 4 years print person is a toddler,
# if at least 4 but less than 13 print person is a kid, if at least 13 but less than 20
# print person is a teenager, if at least 20 but less than 65 print person is an adult,
# and if 65 or older print person is an elder.
age = 65
if age < 2:
    print("the person is a baby.")
elif 2 <= age < 4:
    print("the person is a toddler.")
elif 4 <= age < 13:
    print("the person is a kid.")
elif 13 <= age < 20:
    print("the person is a teenager.")
elif 20 <= age < 65:
    print("the person is an adult.")
else:
    print("the person is an elder")


# 5) Write a function that takes an argument, check this argument to see if it is
# a Boolean using the bool method. Call the method and use the bellow values as your
# arguments. Using comments, provide the name of the arguments and if it was true or false
# from running the code. Values are 12, 1.2, 0, 0.4, and 0.0.
def boolean_check(arg):
    result = bool(arg)
    print(result)


# Value 12, result is true
boolean_check(12)

# Value 1.2, result is true
boolean_check(1.2)

# Value is 0, result is false
boolean_check(0)

# Value is 0.4, result is true
boolean_check(0.4)

# Value is 0.0, result is false
boolean_check(0.0)
