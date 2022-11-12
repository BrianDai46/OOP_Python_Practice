class Rectangle:
    def __init__(self, x, y, height, width, color):
        self.width = width
        self.height = height
        self.color = color
        self.y = y
        self.x = x

    def draw(self, canvas):
        """Draw itself into Canvas"""
        canvas.data[self.x: self.x + self.height, self.y: self.y + self.width] = self.color


class Square:
    def __init__(self, x, y, side, color):
        self.side = side
        self.color = color
        self.y = y
        self.x = x

    def draw(self, canvas):
        """Draws itself into the Canvas"""
        canvas.data[self.x: self.x + self.side, self.y: self.y + self.side] = self.color
