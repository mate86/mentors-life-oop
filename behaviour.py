import random


class Behaviour:

    def eating(self, energy_level=None):
        return random.randrange(1, 5)

    def tell_joke(self, students):
        joke_list = ["What did one wall say to the other?\nMeet you at the corner!",
                     "How did the hipster burn his mouth?\nHe sipped his coffee before it was cool!",
                     "What type of music do mummies listen to?\nWRAP MUSIC!"]
        print("%s" % joke_list[random.randint(0, len(joke_list) - 1)])
        for i in students:
            i.energy_level += random.randint(5, 10)
        return students
