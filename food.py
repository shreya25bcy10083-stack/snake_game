import random

class Food:
    def __init__(self):
        self.positions = []

    def get_random_position(self):
        return (random.randint(0, 29), random.randint(0, 29))

    def spawn_food(self, count):
        self.positions = []
        for _ in range(count):
            self.positions.append(self.get_random_position())
