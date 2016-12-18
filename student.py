import os
from person import Person
from studentactions import StudentActions


class Student(Person):

    def __init__(self, first_name, last_name, year_of_birth, gender, knowledge_level, energy_level):
        super().__init__(first_name, last_name, year_of_birth, gender)
        self.knowledge_level = knowledge_level  # integer
        self.energy_level = energy_level  # integer
        self.studentactions = StudentActions()  # instantiate StudentActions

    @classmethod
    def create_by_csv(cls, filename):
        main_path = os.path.dirname(os.path.abspath(__file__))
        with open(main_path + filename, 'r+') as f:
            lines = f.readlines()
            student_list = []
            for line in lines:
                line = line.rstrip("\n")
                data = line.split(",")
                student_list.append(
                    Student(data[0], data[1], int(data[2]),
                            data[3], int(data[4]), int(data[5])))
        return student_list
