class Pipe
    def __init__ (self, x, y, length, width):
        self.x = x
        self.y = y
        self.height = height 
        self.width = width

    def update(increment):
        self.x += increment

    def doesCollide?(x,y):
        if (x > self.x and x < self.x + self.width) and 
           (y > self.y and y < self.y + self.height):
               return True

        return False
