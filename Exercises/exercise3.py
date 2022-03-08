# Exercise 3 All About Strings

# 2 - 3 Personal Message

# Use a variable to represent a person's name and print a simple message to said person
name = "Samantha"
print(f"Hello {name.title()}, I hope you are enjoying your day.")


# 2 - 4 Name Cases

# Use a variable to represent a person's name and then print the name in
# lowercase, uppercase, and titlecase
name2 = "Eric Scott"
print(name2.lower())
print(name2.upper())
print(name2.title())


# 2 - 5 Famous Quote

# Find a quote from a famous person. Print the quote and
# the name of the author with the quote in quotation marks.
print('Winston S. Churchill once said, "Success is not final; failure is not fatal: '
      'It is the courage to continue that counts."')


# 2 - 6 Famous Quote 2

# Repeat exercise 2-5 but this time use variables for the name and the message,
# with famous_person and message as the variable names and then print
famous_person = 'Winston S. Churchill'
message = '"Success is not final; failure is not fatal: It is the courage to continue that counts."'
print(f'{famous_person} once said, {message}')


# 2 - 7 String/Stripping Names

# Use a variable to represent a person's name and include some whitespaces before and after the name.
# Make sure to use each character combination, \t and \n at least once.
# print the name once so all the whitespaces are shown and then print using each of the three
# stripping functions, lstrip(), rstrip(), and strip().
name3 = "\t Saiki Kusuo \n"
print(name3)
print(name3.lstrip())
print(name3.rstrip())
print(name3.strip())
