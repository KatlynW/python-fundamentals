# User Only for Importing
class User:
    def __init__(self, first_name, last_name, username, gender):
        self.first_name = first_name
        self.last_name = last_name
        self.username = username
        self.gender = gender

    def describe_user(self):
        print(self.username)
        print(self.first_name)
        print(self.last_name)
        print(self.gender)

    def greet_user(self):
        print(f"Welcome, {self.first_name} {self.last_name}.")

