class Pipe:
    def __init__ (self, x, y, height, width):
        self.x = x
        self.y = y
        self.height = height 
        self.width = width

    def update(increment):
        self.x += increment

    def doesCollide(self, x, y, gap):
        if ((x > self.x and x < self.x + self.width) and 
           ((y > self.y and y < self.y + self.height) or
           (y > 0 and y < self.y - gap))):
               return True

        return False
