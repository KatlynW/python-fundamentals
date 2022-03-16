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


class HotBloodedHorse (Horse):
    def __init__(self, age, hoof_angle, hair_length, speed, endurance):
        super().__init__(age, hoof_angle, hair_length)
        self._speed = speed
        self._endurance = endurance

    def racing_not_racing(self):
        return "The {0} year old horse is racing.".format(self.age)

    @property
    def speed(self):
        return self._speed

    @speed.setter
    def speed(self, mph):
        self._speed = mph

    @property
    def endurance(self):
        return self._endurance

    @endurance.setter
    def endurance(self, measure):
        self._endurance = measure


class ColdBloodedHorse (Horse):
    def __init__(self, age, hoof_angle, hair_length, strength, durability):
        super().__init__(age, hoof_angle, hair_length)
        self._strength = strength
        self._durability = durability

    def pulling_not_pulling(self):
        return "The {0} year old horse is pulling something.".format(self.age)

    @property
    def strength(self):
        return self._strength

    @strength.setter
    def strength(self, measures):
        self._strength = measures

    @property
    def durability(self):
        return self._durability

    @durability.setter
    def durability(self, measure):
        self._durability = measure


horse1 = HotBloodedHorse(3, 50, 5, 25, 20)
horse2 = ColdBloodedHorse(5, 40, 10, 40, 30)
print(horse1.endurance)
print(horse1.racing_not_racing())
print(horse2.strength)
print(horse2.pulling_not_pulling())
