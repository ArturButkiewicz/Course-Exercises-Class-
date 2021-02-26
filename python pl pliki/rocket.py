from random import randint
from math import sqrt


class Rocket:
    def __init__(self, speed: float = 1, altitude: float = 0, x: float = 0):
        self.altitude = altitude

        self.speed = speed

        self.x = 0

    def move_up(self):
        self.altitude += self.speed

    def __str__(self):
        return "Rakieta jest aktualnie na wysokości: " + str(self.altitude)


class RocketBoard:
    def __init__(self, amountOfRockets=5):
        self.rockets = [Rocket(randint(1, 6)) for _ in range(amountOfRockets)]

        for _ in range(10):
            rocketIndexToMove = randint(0, len(self.rockets) - 1)
            self.rockets[rocketIndexToMove].move_up()

        for rocket in self.rockets:
            print(rocket)

    def __getitem__(self, key):
        return self.rockets[key]

    def __setitem__(self, key, value):
        self.rockets[key].altitude = value

    @staticmethod
    def get_distance(obj: Rocket, obj2: Rocket) -> float:
        ac = (obj.altitude - obj2.altitude) ** 2
        bc = (obj.x - obj2.x) ** 2

        return sqrt(ac + bc)
    
    def get_amount_of_rockets(self):
        return len(self.rockets)

    def __len__(self):
        return self.get_amount_of_rockets()

