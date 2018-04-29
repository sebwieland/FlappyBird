class Bird:
    def __init__(self):
        print("init bird")
        self.y = height / 2.
        self.x = 100.

        self.gravity = 0.6
        self.lift = -10
        self.velocity = 0

        self.width = 32.
        self.height = 32.

        # self.score = 0

    def show(self):
        ellipse(self.x - self.width / 2., self.y -
                self.height/2., self.width, self.height)

    def up(self):
        if (self.velocity >= 0):
            self.velocity = self.lift

    def update(self):
        self.velocity += self.gravity
        self.y += self.velocity

    def offscreen(self):
        return (self.y - self.height/2. < 0 or self.y - self.height/2. > height)

    def reset(self):
        self.y = height / 2.
        self.velocity = 0
