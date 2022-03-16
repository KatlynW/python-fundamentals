# Exercise 8 - Collections

# 1) Do 5 - 8 and 5 - 9

# 5 - 8 Hello Admin
# make a list of 5 or more usernames, including the name 'admin'. create a code that
# wil print a greeting to each user after they log in and loop through the list to print
# the greeting to each user. If the username is 'admin' put a special greeting, otherwise
# print a generic greeting.
usernames = ["john", "may", "mark", "lee", "jane", "admin"]
for name in usernames:
    if name == "admin":
        print(f"Hello {name}, would you like to see a status report?")
    else:
        print(f"Hello {name}, thank you for logging in again.")

# 5 - 9 No Users
# Add an if statement to make sure the list of users is not empty. If it is empty,
# print the message "We need to find some users!" Then remove all the usernames from
# the list to make sure the correct message is printed.
# Since I kept the previous loop for 5-8 and created a copy, I simply left the code
# as cleared.
usernames.clear()
if len(usernames) == 0:
    print("We need to find some users!")
else:
    for name in usernames:
        if name == "admin":
            print(f"Hello {name}, would you like to see a status report?")
        else:
            print(f"Hello {name}, thank you for logging in again.")


# 2) 5 - 10 Checking Usernames
# Make a list of 5 or more usernames called "current_users". Make another list
# of 5 usernames called new_users, make sure one or two of these usernames are
# also in the current_users list. Loop through the new_users list to check if
# the username has already been used, if it has print a message that the person
# will need to enter a new username, if it has not been used, print that it is
# available. Make sure the comparison is case-sensitive so if 'John' is already
# used, 'JOHN' will not be accepted.
# In this case, to adapt to any changes I made to the current_users list, I made an
# empty list and then user lower() to make the list inserts lowercase.
current_users = ["Mary", "May", "Eric", "Tulip", "Frank"]
current_users_lower = []
for case in current_users:
    current_users_lower.append(case.lower())
new_users = ["MAY", "Rose", "June", "Tulip", "Pepper"]
for user in new_users:
    if user.lower() in current_users_lower:
        print("Sorry, that username is taken, please enter a new username.")
    else:
        print("That username is available.")


# 3) 5 - 11 Ordinal Numbers:
# ordinal numbers indicate their position in a list, such as 1st or 2nd. Most
# of these end in th, except of 1, 2, and 3. Store the numbers 1 through 9 in
# a list. Loop through this list. Use an if-elif-else chain inside the loop
# to print the proper ordinal ending for each number. It should output "1st 2nd
# 3rd 4th 5th 6th 7th 8th 9th" wit each result on a separate line.
ordinal_numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
for number in ordinal_numbers:
    if number == 1:
        print(f"{number}st")
    elif number == 2:
        print(f"{number}nd")
    elif number == 3:
        print(f"{number}rd")
    else:
        print(f"{number}th")


# 4) 6 - 1 Person
# Use a dictionary to store information about a person you know.
# Store their first name, last name, age, and city. Then print each
# piece of information stored in the dictionary.
person = {
    "first_name": "Brynn",
    "last_name": "Adams",
    "age": 26,
    "city": "Wichita"
}
for info, answer in person.items():
    print(f"{info} : {answer}")


# 5) 6 - 7 People
# Start with program from 6-1, make 2 more dictionaries for separate
# people and store all three in list people. Loop through the list and
# print everything you know about each person.
person1 = {
    "first_name": "Brynn",
    "last_name": "Adams",
    "age": 26,
    "city": "Wichita"
}
person2 = {
    "first_name": "Andy",
    "last_name": "Lee",
    "age": 20,
    "city": "Wichita"
}
person3 = {
    "first_name": "Scott",
    "last_name": "Chhan",
    "age": 26,
    "city": "Wichita"
}
people = [person1, person2, person3]
for name in people:
    for info, answer in name.items():
        print(f"{info} : {answer}")
