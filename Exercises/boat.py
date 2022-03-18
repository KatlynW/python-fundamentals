# Boat Class

class Boat:
    def __init__(self, wood_color, wood_type, plank_size):
        self._wood_color = wood_color
        self._wood_type = wood_type
        self._plank_size = plank_size

    def boat_dock_undock(self):
        print(str.format('The {0} boat is docked', self._wood_color))

    def wood_color_func(self):
        return self._wood_color

    # getter
    def get_wood_color(self):
        return self._wood_color

    # setter
    def set_wood_color(self, color):
        self._wood_color = color

    # deleter
    def del_wood_color(self):
        del self._wood_color

    # creating the property
    wood_color = property(get_wood_color, set_wood_color, del_wood_color)

    def wood_type_func(self):
        return self._wood_type

    # getter
    def get_wood_type(self):
        return self._wood_type

    # setter
    def set_wood_type(self, type):
        self._wood_type = type

    # deleter
    def del_wood_type(self):
        del self._wood_type

    # creating the property
    wood_type = property(get_wood_type, set_wood_type, del_wood_type)

    def plank_size_func(self):
        return self._plank_size

    # getter
    def get_plank_size(self):
        return self._plank_size

    # setter
    def set_plank_size(self, size):
        self._plank_size = size

    # deleter
    def del_plank_size(self):
        del self._plank_size

    # creating the property
    plank_size = property(get_plank_size, set_plank_size, del_plank_size)


my_boat = Boat('Pink', 'Acacia', 12)
print(my_boat.get_wood_color())
my_boat.set_wood_color('Brown')
print(my_boat.get_wood_color())
print(my_boat.boat_dock_undock())
