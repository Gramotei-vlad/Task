class Polygon:
    def perimeter(self):
        pass

    def area(self):
        pass


class Rectangle(Polygon):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def perimeter(self):
        return (self.width + self.height) * 2

    def area(self):
        return self.width * self.height


class Square(Polygon):
    def __init__(self, side):
        self.side = side

    def perimeter(self):
        return self.side * 4

    def area(self):
        return self.side * self.side