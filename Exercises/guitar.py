# Guitar Class

class Guitar:
    def __init__(self, wood_color, wood_type, neck_size):
        self._wood_color = wood_color
        self._wood_type = wood_type
        self._neck_size = neck_size

    def string_vibrating_not_vibrating(self):
        print(str.format("The {0} guitar's strings are vibrating", self._wood_color))

    @property
    def wood_color(self):
        return self._wood_color

    @wood_color.setter
    def wood_color(self, color):
        self._wood_color = color

    @property
    def wood_type(self):
        return self._wood_type

    @wood_type.setter
    def wood_type(self, wood_type):
        self._wood_type = wood_type

    @property
    def neck_size(self):
        return self._neck_size

    @neck_size.setter
    def neck_size(self, size):
        self._neck_size = size


my_guitar = Guitar("brown", "Cedar", 10)
print(my_guitar.neck_size)
print(my_guitar.string_vibrating_not_vibrating())
my_guitar.neck_size = 20
print(my_guitar.neck_size)
