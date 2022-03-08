# Exercise 5 Operators

# 1) 5 - 1 Conditional Test
# Write a series of conditional tests. Print a statement describing each test and your prediction
# for the results of each test. Make sure you understand why it gives the evaluations. Create at
# least 10 tests total, 5 true, 5 false.

# snake tests (1 and 2)
snake = "python"
print("Is snake == 'python'? I predict true.")
print(snake == "python")
print("Is snake == 'mamba?' I predict False")
print(snake == "mamba")

# cat tests (3 and 4)
cat = "feral"
print("Is cat == 'domestic'? I predict True")
print(cat == "domestic")
print("Is cat ==  'feral'? I predict False")
print(cat == "feral")

# plane tests (5 and 6)
plane = "domestic"
print("Is plane == 'domestic'? I predict true.")
print(plane == "domestic")
print("Is plane == 'international?' I predict False")
print(snake == "international")

# suitcase tests (7 and 8)
suitcase = "closed"
print("Is suitcase == 'open'? I predict true.")
print(suitcase == "open")
print("Is suitcase == 'closed?' I predict False")
print(suitcase == "closed")

# box tests (9 and 10)
box = "open"
print("Is box == 'open'? I predict true.")
print(box == "open")
print("Is box == 'sealed?' I predict False")
print(box == "sealed")


# 2) 5 - 2 More Conditional Tests
# You don't have to limit the number of tests to 10. IF you want to ty more comparisons, write more.
# Have at least one True and one False result for each of the following.

# a) Tests for equality and inequality with strings
name = "Susan"
print("Is name == 'Susan'? I predict true.")
print(name == "Susan")
name = "Ricky"
print("Is name != 'Ricky'? I predict false.")
print(name != "Ricky")
# b) Tests using the .lower method
case = "CAPITAL"
print("Is case == case.lower? I predict true.")
print(case == case.lower())
case = "capital"
print("Is case == case.lower? I predict false.")
print(case == case.lower())
# c) Numerical tests involving equality and inequality, greater than and less than, greater than
# or equal to, and less than or equal to
number = 11
print("Is number < 20? I predict true.")
print(number < 20)
print("Is number >= 15? I predict false.")
print(number >= 15)
# d) Test using the and keyword and the or keyword
name1, name2 = "Mark", "Suzy"
print("Is name1 == 'Mark' and name2 == 'Patrick?' I predict false.")
print(name1 == "Mark" and name2 == "Patrick")
print("Is name1 'Paul' or name2 == 'Suzy'? I predict true.")
print(name1 == "Mark" or name2 == "Suzy")
# e) Test whether an item is in a list
list1 = 15, 42, "Square"
print("Is 23 in list1? I predict true.")
print(23 in list1)
print("Is 'Square' in list1? I predict false.")
print("Square" in list1)
# f) Test whether an item in not in a list
list2 = 24, 74, "Fake", "Lose"
print("Is 'Jane' not in list2? I predict true.")
print("Jane" not in list2)
print("is 74 not in list2? I predict false.")
print(74 not in list2)


# 3) Write a function that takes two arguments. Inside provide examples of all
# the arithmetic operators. Provide a variable for each solution and print
# the results of each.
def arithmetic_operators(num1, num2):
    add_sum = num1 + num2
    subtract_sum = num2 - num1
    multi_sum = num1 * num2
    divide_sum = num2 / num1
    modulus_sum = num1 % 5
    exponent_sum = num2 ** 3
    floor_divide_sum = num2 // 2

    # print the sums
    print(add_sum)
    print(subtract_sum)
    print(multi_sum)
    print(divide_sum)
    print(modulus_sum)
    print(exponent_sum)
    print(floor_divide_sum)


arithmetic_operators(23, 42)


# 4) Write a function that takes one argument. Inside provide examples of modulus equals,
# minus equals, exponent equals, and plus equals. Provide a variable for each solution and print.
def assign_operators(num1):
    num1 %= 2
    print(num1)
    num1 -= 4
    print(num1)
    num1 **= 5
    print(num1)
    num1 += 10
    print(num1)


assign_operators(257)
