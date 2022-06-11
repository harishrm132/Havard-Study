import random

# Singleton
# Class Method - Like Factory methods in C#

class Hat:

    houses = ["Gryffindor", "HufflePuff", "RavenClaw", "Slytherin"]

    @classmethod
    def sort(cls, name):
        print(name, "is in", random.choice(cls.houses))


Hat.sort("Harry")