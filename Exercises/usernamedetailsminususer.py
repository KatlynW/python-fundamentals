# Everything username minus User

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
