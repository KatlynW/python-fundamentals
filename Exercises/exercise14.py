# Exercise 14 Testing Code
import unittest

# Write each in a function and then call it.


# 1) 11 - 1 City, Country
# Write a function that accepts two parameters: a city name and a country name.
# The function should return a single string in the form of City, Country. store
# the function in a module called city_functions.py Create a file called test_cities.py
# that tests the function you just wrote with unittest. Write a method called
# test_city_country() to verify that calling with the appropriate values runs correctly.
def city_country(city_name, country_name):
    return "{0}, {1}".format(city_name, country_name)


# 2) 11 - 2
# Modify the above to have a third parameter, population.
def city_country2(city_name, country_name, population=" "):
    return "{0}, {1} - population {2}".format(city_name, country_name, population)


# 3) 11 - 3 Employee
# Write a class called Employee. THe __init__() method should take first_name,
# last_name, annual_salary and store then as attributes. Write a method called
# give_raise() that adds 5000 to annual salary by default but accepts other values.
# Test the class.
class Employee:
    def __init__(self, first_name, last_name, annual_salary):
        self._first_name = first_name
        self._last_name = last_name
        self._annual_salary = annual_salary

    def __str__(self):
        return f"{self._first_name} {self._last_name} {self._annual_salary}"

    def give_raise(self, amount=5000):
        self._annual_salary = str(int(self._annual_salary) + amount)
        return f"{self._first_name} {self._last_name} {self._annual_salary}"


class TestingExercises(unittest.TestCase):
    def test_city_country(self):
        formatted_city = city_country("New York", "The United States")
        self.assertEqual(formatted_city, "New York, The United States")

    def test_city_country2(self):
        formatted_city_2 = city_country("New York", "The United States - population 50000")
        self.assertEqual(formatted_city_2, "New York, The United States - population 50000")

    def setUp(self):
        self. my_employee = Employee("Jane", "Foster", 500000)

    def test_give_default_raise(self):
        self.my_employee.give_raise()
        self.employee1 = self.my_employee.__str__()
        self.assertEqual(self.employee1, "Jane Foster 505000")

    def test_give_custom_raise(self):
        self.my_employee.give_raise(10000)
        self.employee1 = self.my_employee.__str__()
        self.assertEqual(self.employee1, "Jane Foster 510000")


if __name__ == "__main__":
    unittest.main()
