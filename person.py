from energizing import Energizing
from behaviour import Behaviour


class Person:

    def __init__(self, first_name, last_name, year_of_birth, gender):
        self.first_name = first_name
        self.last_name = last_name
        self.year_of_birth = year_of_birth
        self.gender = gender
        self.energizing = Energizing()
        self.behaviour = Behaviour()

    def check_value_error(self):
        if first_name is None or last_name is None or year_of_birth is None:
            raise ValueError
        if gender != male or gender != female or gender != notsure:
            raise ValueError
