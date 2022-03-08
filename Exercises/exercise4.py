# Exercise 4 All About Numbers

# 1) Do Exercises 2-8 and 2-9

# 2 - 8 Number Eight
# Write addition, subtraction, multiplication, and division operations
# that all result in the number 8. Enclose these in print statements.
print(6 + 2)
print(12 - 4)
print(4 * 2)
print(int(24 / 3))


# 2 - 9 Favorite Number
# Use a variable to represent your favorite number. Then use that variable
# to create a message revealing your favorite number. Print the message.
fav_number = 11
message = f"My favorite number is {fav_number}."
print(message)


# 2) Assign variables to the following sets of numbers. Use underscores
# to make them more readable. Write a function called number_sets and print
# each variable inside the function. Then call the function to check.
# a) 456234, b) 68423791, c) 13794628, d) 96374
number1 = 456_234
number2 = 68_423_791
number3 = 13_794_628
number4 = 96_374


def number_sets():
    print(number1)
    print(number2)
    print(number3)
    print(number4)


number_sets()


# 3) Write a function that will take two arguments. Using Type conversion, convert the first
# argument from an int to a float. Convert the second from float to int. Call the function
# and provide the correct values for each argument to verify your results.
def conversion(first_number, second_number):
    first_number = float(first_number)
    second_number = int(second_number)
    print(type(first_number), type(second_number))


conversion(8, 4.2)


# 4) Write a function that will have 2 inputs. The first should ask "What is your favorite movie?"
# and the second should ask "How many times have you seen it?" Each input should be assigned to a
# variable. In a print statement with placeholders, the output result should be "I have seen
# {favorite movie} {number of time} times."
def fav_movie():
    movie_name = input("What is your favorite movie? ")
    times_watched = input("How many times have you watched it? ")
    print(f"I have seen {movie_name} {times_watched} times.")


fav_movie()
