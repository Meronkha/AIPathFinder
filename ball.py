class Ball:
    def __init__(self, x, y, speed, gravity):
        self.x = x
        self.y = y
        self.speed = speed
        self.gravity = gravity


    def update(self):
        self.y += self.speed
        self.speed += self.gravity
