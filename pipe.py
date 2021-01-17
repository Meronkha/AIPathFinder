class Pipe:
    def __init__ (self, x, y, height, width):
        self.x = x
        self.y = y
        self.height = height 
        self.width = width

    def update(increment):
        self.x += increment

    def doesCollide(self, x, y, gap, radius):
        x_upper = x + radius
        y_lower = y - radius 
        y_upper = y + radius 
        if ((x_upper > self.x and x_upper < self.x + self.width) and 
           ((y_upper > self.y) or
           (y_lower < self.y - gap))):
               return True

        return False
