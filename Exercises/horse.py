# Horse Class

class Horse:
    def __init__(self, age, hoof_angle, hair_length):
        self._age = age
        self._hoof_angle = hoof_angle
        self._hair_length = hair_length

    def horse_lay_down_get_up(self):
        print(str.format('The {0} year old horse is laying down', self._age))

    @property
    def age(self):
        return self._age

    @age.setter
    def age(self, num):
        self._age = num

    @property
    def hoof_angle(self):
        return self._hoof_angle

    @hoof_angle.setter
    def hoof_angle(self, angle):
        self._hoof_angle = angle

    @property
    def hair_length(self):
        return self._hair_length

    @hair_length.setter
    def hair_length(self, length):
        self._hair_length = length


my_horse = Horse(5, 50, 10)
print(my_horse.hair_length)
print(my_horse.horse_lay_down_get_up())
