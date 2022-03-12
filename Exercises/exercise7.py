# Exercise 7 Looping

# Write function for each of the items below and call them to ensure the results are correct.

# 1) 4 - 3 Counting to Twenty
# Use a for loop to print the numbers 1 to 20, inclusive.
def count_to_twenty():
    # Note: make sure to have the end number be 21, not 20, so it includes 20.
    for num1 in range(1, 21):
        print(num1)


count_to_twenty()


# 2) 4 - 6 Odd Numbers
# Use the thord argument of the range() function to make a list of the odd numbers from
# 1 to 20, use a for loop to print each number.
def odd_numbers():
    for num2 in range(1, 20, 2):
        print(num2)


odd_numbers()


# 3) 4 - 7 Threes
# Make a list of the multiples of 3 from 3 to 30. Use a for loop to print the numbers
# in that list.
def multiples_of_three():
    # Note: the following line uses the range of the numbers 3 to 31, to include 30,
    # and the increment of 3, to then make it into a list and define this range to a list
    multiples = list(range(3, 31, 3))
    for num3 in multiples:
        print(num3)


multiples_of_three()


# 4) 4 - 8 Cubes
# A number raised to the third power is called  cube, for example, the cube of 2 is written
# as 2**3 in Python. Make a list of the first 10 cubes (that is the cube of each integer from
# 1 through 10), and use a for loop to print out the value of each cube.
def first_10_cubes():
    # The following code is an adaptation to the example shown in the book at the top of page
    # 59. This code below creates an empty list, cubes, and then add the cubes of each number from
    # 1 through 10 to the list via a for loop that uses the range of 1 to 11, which doesn't include 11,
    # to then add/append each number cubed to the list.
    cubes = []
    for num4 in range(1, 11):
        cubes.append(num4**3)
    # The code below is another for loop that uses the previously made list to print each cube on its own.
    for cube in cubes:
        print(cube)


first_10_cubes()
