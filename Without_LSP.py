class Rectangle:
    def __init__(self):
        self.width = 0
        self.height = 0

    def setWidth(self, width):
        self.width = width

    def setHeight(self, height):
        self.height = height

    def perimeter(self):
        return (self.width + self.height) * 2

    def area(self):
        return self.width * self.height


class Square(Rectangle):
    def __init__(self):
        super().__init__()

    def setWidth(self, width):
        self.width = width
        self.height = width

    def setHeight(self, height):
        self.height = height
        self.width = height


def test(rectangle):
    assert rectangle.perimeter() == 30
    assert rectangle.area() == 56
    return 'OK'


rectangle_1 = Rectangle()
rectangle_1.setWidth(7)
rectangle_1.setHeight(8)
square_1 = Square()
square_1.setWidth(7)
square_1.setHeight(8)
print(test(rectangle_1))
print(test(square_1))  # Тут не пройдет assert => нарушение lsp
