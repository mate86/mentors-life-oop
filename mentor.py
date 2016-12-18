import os
from person import Person
from education import Education


class Mentor(Person):

    def __init__(self, first_name, last_name, year_of_birth, gender, nickname):
        super().__init__(first_name, last_name, year_of_birth, gender)
        self.nickname = nickname
        self.educate = Education()

    @classmethod
    def create_by_csv(cls, filename):
        main_path = os.path.dirname(os.path.abspath(__file__))
        with open(main_path + filename, 'r+') as f:
            lines = f.readlines()
            mentor_list = []
            for line in lines:
                line = line.rstrip("\n")
                data = line.split(",")
                mentor_list.append(
                    Mentor(data[0], data[1], data[2], data[3], data[4]))
        return mentor_list
