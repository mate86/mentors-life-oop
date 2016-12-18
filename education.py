import random


class Education:

    def teaching(self):  # not implemented
        raise NotImplementedError()

    def motivational_speak(self, students):
        for i in students:
            i.energy_level += random.randint(5, 10)
        print("The mentor gives a motivational speech like no other!\n")

    def ring_bell(self):
        print("\n(The Bell is ringing!)")
