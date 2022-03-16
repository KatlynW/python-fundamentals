# Watch Class

class Watch:
    def __init__(self, indice_type, base_color, hand_material):
        self._indice_type = indice_type
        self._base_color = base_color
        self._hand_material = hand_material

    def watch_turn_on_turn_off(self):
        print(str.format('The {0} watch is on', self._base_color))

    @property
    def indice_type(self):
        return self._indice_type

    @indice_type.setter
    def indice_type(self, type):
        self._indice_type = type

    @property
    def base_color(self):
        return self._base_color

    @base_color.setter
    def base_color(self, color):
        self._base_color = color

    @property
    def hand_material(self):
        return self._hand_material

    @hand_material.setter
    def hand_material(self, material):
        self._hand_material = material


my_watch = Watch("Roman Numerals", "black", 'gold')
print(my_watch.hand_material)
print(my_watch.watch_turn_on_turn_off())
