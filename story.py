from codecool_class import CodecoolClass
from mentor import Mentor
from student import Student
import random


def study_func(cc_budapest):
    # This function couts the knowledge level before and after studying
    total_knowledge = 0
    for i in cc_budapest.students:
        total_knowledge += i.knowledge_level
    average_knowledge = total_knowledge / len(cc_budapest.students)

    print("\nThe average knowledge is: %.2f\n" % average_knowledge)
    total_energy = 0
    total_knowledge = 0
    for i in cc_budapest.students:
        print(i.first_name + " " + i.last_name, "is studying: ", end=' ')
        modified_level = i.studentactions.study()
        i.energy_level += modified_level
        i.knowledge_level -= modified_level
        total_energy += i.energy_level
        total_knowledge += i.knowledge_level
        if i.energy_level < 5:
            i.energy_level = 5
    average_energy = total_energy / len(cc_budapest.students)
    average_knowledge = total_knowledge / len(cc_budapest.students)
    print("\nStudying is exhausting, so energy level drops to: %.2f" %
          average_energy)
    print("The average knowledge level increased to: %.2f" % average_knowledge)


def main():
    print("Goodmorning Codecoolers! A new day is here!\n")
    input()
    cc_budapest = CodecoolClass.generate_local()
    mentor_immi = cc_budapest.find_mentor_by_full_name("Immánuel Fodor")
    mentor_laci = cc_budapest.find_mentor_by_full_name("László Molnár")
    mentor_matyi = cc_budapest.find_mentor_by_full_name("Mátyás Forián Szabó")
    mentor_zoli = cc_budapest.find_mentor_by_full_name("Zoltán Sallay")
    input()
    # attendance is coming
    print("\nBrace yourself, attendance is coming")
    input()

    total_energy = 0
    for i in cc_budapest.students:
        print("Is %s %s here?" % (i.first_name, i.last_name))
        print("Yup, and my energy is: {}".format(i.energy_level))
        total_energy += int(i.energy_level)
    average_energy = total_energy / len(cc_budapest.students)
    print("Great, everyone is here\n")

    print("The average energy of the students: %.2f \nLet's do some gymnastics to raise it!" % average_energy)

    input()

    print("The Students are doing some gymnastics...")

    total_energy = 0
    for i in cc_budapest.students:
        i.energy_level += i.energizing.do_gymnastics()
        total_energy += int(i.energy_level)
    average_energy = total_energy / len(cc_budapest.students)

    print("The average energy of the students increased to: %.2f\n" %
          average_energy)

    input()

    print("Well.... that's not much better, let's drink some coffee")

    total_energy = 0
    total_knowledge = 0
    for i in cc_budapest.students:
        i.energy_level += i.energizing.drink_coffee()
        total_energy += int(i.energy_level)
        total_knowledge += i.knowledge_level
    average_energy = total_energy / len(cc_budapest.students)
    average_knowledge = total_knowledge / len(cc_budapest.students)

    print("The Student has drunk some coffee.")
    print("The average energy of the students increased to: %.2f" % average_energy)

    input()

    print("Mentor: Now, please improve the topic you think you can polish your knowledge at")
    study_func(cc_budapest)

    input()

    mentor_immi.educate.ring_bell()
    print("It's 11:45, it's time to eat!\n")

    input()

    total_energy = 0
    print("Students are enjoying food")
    for i in cc_budapest.students:
        i.energy_level += i.behaviour.eating()
        total_energy += int(i.energy_level)
    average_energy = total_energy / len(cc_budapest.students)
    print("The average energy of the students increased to: %.2f" % average_energy)
    print("It's 13:00.\nYummie! The lunch was nice, but now we need some motivation\n")

    input()

    mentor_immi.educate.motivational_speak(cc_budapest.students)

    input()
    print("The Mentor is telling a joke: ", sep=" ")
    laughing_students = mentor_immi.behaviour.tell_joke(cc_budapest.students)
    for i in laughing_students:
        i.energy_level += random.randint(1, 5)

    print("\nBadabummTssss!\nThe joke energized the Students")

    input()

    print("Oooo... it seems like guys are starting to behave badly...\n")
    for i in cc_budapest.students:
        if i.gender == "male":
            print(i.first_name + " " + i.last_name + " " + "is", end=' ')
            i.energy_level += i.studentactions.bad_behaviour()
            print(i.first_name +
                  "'s energy level raises to: ", i.energy_level)
            print("\n")

    input()

    study_func(cc_budapest)

    input()
    mentor_immi.educate.ring_bell()
    print("It's time to go home")


# Main program
main()
