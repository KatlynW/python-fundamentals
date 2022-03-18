# Watch Class

class Watch:
    def __init__(self, indice_type, base_color, hand_material):
        self._indice_type = indice_type
        self._base_color = base_color
        self._hand_material = hand_material

    def watch_turn_on_turn_off(self):
        print(str.format('The {0} watch is on', self._base_color))

    def indice_type_func(self):
        return self._indice_type

    # getter
    def get_indice_type(self):
        return self._indice_type

    # setter
    def set_indice_type(self, type):
        self._indice_type = type

    # deleter
    def del_indice_type(self):
        del self._indice_type

    # creating the property
    indice_type = property(get_indice_type, set_indice_type, del_indice_type)

    def base_color_func(self):
        return self._base_color

    # getter
    def get_base_color(self):
        return self._base_color

    # setter
    def set_base_color(self, color):
        self._base_color = color

    # deleter
    def del_base_color(self):
        del self._base_color

    # creating the property
    base_color = property(get_base_color, set_base_color, del_base_color)

    def hand_material_func(self):
        return self._hand_material

    # getter
    def get_hand_material(self):
        return self._hand_material

    # setter
    def set_hand_material(self, mat):
        self._hand_material = mat

    # deleter
    def del_hand_material(self):
        del self._hand_material

    # creating the property
    hand_material = property(get_hand_material, set_hand_material, del_hand_material)


my_watch = Watch("Roman Numerals", "black", 'gold')
print(my_watch.get_hand_material())
my_watch.set_hand_material('iron')
print(my_watch.get_hand_material())
print(my_watch.watch_turn_on_turn_off())
