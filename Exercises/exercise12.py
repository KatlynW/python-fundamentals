# Exercise 12 Exception Handling

# Write functions for each, call the functions to verify.

# 1) 10 - 6 Addition
# One common problem when prompting for numerical input occurs when people
# provide text instead of numbers and when you try to convert it, you get
# ValueError. Wrote a program that prompts for two numbers, add them together,
# and print the result. Catch the ValueError if either input is not a number and
# print a friendly error message, test this with two numbers and then with some text.
def addition():
    try:
        print("Let's do some addition! ")
        number1 = input("What is the first number? ")
        number2 = input("What is the second number? ")
        result = int(int(number1) + int(number2))
        print(result)
    except ValueError:
        print("That is not a number")

# commented out for ease of further programming
# addition()


# 2) 10 - 7 Addition Calculator
# Wrap the code from 10-6 in a while loop so the user can continue
# entering numbers even if they make a mistake and input text instead of a number.
def addition_calculator():
    addition_loop = "True"
    while addition_loop == "True":
        try:
            print("Let's do some addition! ")
            number1 = input("What is the first number? ")
            number2 = input("What is the second number? ")
            result = int(int(number1) + int(number2))
            print(result)
        except ValueError:
            print("That is not a number")
        finally:
            more = input("Continue? True or False? ")
            addition_loop = bool(more)


# commented out for ease of further programming
# addition_calculator()


# 3) 10 - 8 Cats and Dogs
# Make two files, cats.txt and dogs.txt. Store at least 3 names of cats in the
# first file and three names of dogs in the second file. Write a program that tries
# to read these files and print the contents of the files to the screen. Wrap code
# in a trip-except block to catch the FileNotFound error and print a friendly error
# message. Move one file to a different location and make sure the code in the except
# block executes properly.
def cats_and_dogs():
    try:
        with open('cats.txt', encoding='utf-8') as f:
            contents = f.read()
        with open('dogs.txt', encoding='utf-8') as f:
            contents = f.read()
    except FileNotFoundError:
        print("The File is not found in current location.")


cats_and_dogs()


# 4) 10 - 9 Silent Cats and Dogs
# Modify the except block in exercise 10-8 to fail silently in either file is missing.
def silent_cats_and_dogs():
    try:
        with open('cats.txt', encoding='utf-8') as f:
            contents = f.read()
        with open('../dogs.txt', encoding='utf-8') as f:
            contents = f.read()
    except FileNotFoundError:
        pass


silent_cats_and_dogs()
