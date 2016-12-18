import random


class StudentActions():
    Study_topics = ["OOP in Python",
                    "Ubuntu basics",
                    "Lists and Strings in Python",
                    "Loops in Python",
                    "Functions in Python",
                    "File handling  in Python"]

    # bad_behaviour_actions = ["Screaming in class",
    #                         "Listening to loud music",
    #                         "throwing stuff at each other"]

    # the below methode is implemented cose of the specification...
    def bad_behaviour(self):
        a = random.randrange(1, 3)
        if a == 1:
            print("screaming in class")
        elif a == 2:
            print("listening to loud music")
        else:
            print("throwing stuff around")
        #print(self.bad_behaviour_actions[random.randrange(0, len(self.bad_behaviour_actions))])
        return random.randrange(5, 10)

    def study(self):
        print(self.Study_topics[random.randrange(0, len(self.Study_topics))])
        return random.randrange(-10, -5)
