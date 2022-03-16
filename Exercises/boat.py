# Boat Class

class Boat:
    def __init__(self, wood_color, wood_type, plank_size):
        self._wood_color = wood_color
        self._wood_type = wood_type
        self._plank_size = plank_size

    def boat_dock_undock(self):
        print(str.format('The {0} boat is docked', self._wood_color))

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
    def plank_size(self):
        return self._plank_size

    @plank_size.setter
    def plank_size(self, size):
        self._plank_size = size


my_boat = Boat('Pink', 'Acacia', 12)
print(my_boat.plank_size)
print(my_boat.boat_dock_undock())
