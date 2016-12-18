import random


class Energizing:

    def drink_coffee(self):
        return random.randrange(1, 5)

    def do_gymnastics(self):
        return random.randrange(1, 10)

    def run_around_school(self):  # not implemented
        raise NotImplementedError
