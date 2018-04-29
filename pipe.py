import random
import math
import bird


class Pipe:
    def __init__(self):
        self.spacing = 175
        self.top = random.uniform(height/6., 3./4.*height)
        self.bottom = height - (self.top + self.spacing)

        self.x = float(width)
        self.w = 80
        self.speed = 4

        self.passed = False

    def hits(self, bird):
        if (self.top > bird.y or height - self.bottom < bird.y):
            if (self.x < bird.x and self.x + self.w > bird.x ):
                return True
        return False

    def passes(self, bird):
        if (bird.x > self.x + self.w and not self.passed):
            self.passed = True
            return True
        return False

    def show(self):
        fill(255)
        rect(self.x, 0, self.w, self.top)
        rect(self.x, height - self.bottom, self.w, self.bottom)

    def update(self):
        self.x -= self.speed

    def offscreen(self):
        return (self.x < -self.w)
