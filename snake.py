import random

class Snake:
    def __init__(self, grid):
        self.grid = grid
        self.body = [(grid // 2, grid // 2)]
        self.direction = (1, 0)
        self.grow_pending = 0

    def change_direction(self, direction):
        # Prevent reversing direction
        if (direction[0] * -1, direction[1] * -1) != self.direction:
            self.direction = direction

    def move(self):
        x, y = self.body[0]
        new_head = (x + self.direction[0], y + self.direction[1])
        self.body.insert(0, new_head)

        # Only pop tail if we are not growing
        if self.grow_pending > 0:
            self.grow_pending -= 1
        else:
            self.body.pop()

    def grow(self):
        # Add 1 segment growth
        self.grow_pending += 1

    def check_collision(self):
        x, y = self.body[0]
        return (
            x < 0 or y < 0 or
            x >= self.grid or y >= self.grid or
            self.body[0] in self.body[1:]  # Self collision
        )


class Food:
    def __init__(self, grid, count):
        self.grid = grid
        self.count = count
        self.positions = []
        self.new_positions([])

    def new_positions(self, snake_body):
        spots = [
            (x, y)
            for x in range(self.grid)
            for y in range(self.grid)
            if (x, y) not in snake_body
        ]

        random.shuffle(spots)
        self.positions = spots[:self.count]


