from mentor import Mentor
from student import Student


class CodecoolClass:

    def __init__(self, location, year, mentors, students):
        self.location = location
        self.year = year
        self.mentors = mentors
        self.students = students

    @classmethod
    def generate_local(cls):
        location = "Budapest"
        year = 2016
        mentors = Mentor.create_by_csv("/data/mentors.csv")
        print("Mentors are initialised by CSV")
        students = Student.create_by_csv("/data/students.csv")
        print("Students are initialised by CSV\n")
        print("School @ {} in year {} is created with {} mentors and {} students\n".format(
            location, year, len(mentors), len(students)))
        codecool_object = CodecoolClass(
            location, year, mentors, students)
        return codecool_object

    def find_mentor_by_full_name(self, full_name):
        for line in self.mentors:
            if line.first_name + line.last_name == full_name:
                print("{} was found between the mentors".format(full_name))
                return line

    def find_student_by_full_name(self, full_name):
        for line in self.students:
            fullname = line.first_name + line.last_name
            if full_name == fullname:
                return line
