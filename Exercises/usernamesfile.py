# Usernames details to import
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


class Privileges:
    def __init__(self, privileges):
        self.privileges = list(privileges)

    def show_privileges(self):
        print(self.privileges)


class Admin(User):
    def __init__(self, first_name, last_name, username, gender, privileges):
        super().__init__(first_name, last_name, username, gender)
        self.privileges = privileges2


privileges2 = Privileges(("can ban user", "can unban user", "can remove post"))
admin2 = Admin("Jane", "Matthews", "DoeEyed", "Female", privileges2)
privileges2.show_privileges()

