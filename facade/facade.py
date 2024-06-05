class Shape:
    def draw(self):
        pass
class Rectangle(Shape):
    def draw(self):
        print("rectangle")

class Circle(Shape):
    def draw(self):
        print('circle')
class ShapeMaker:
    def __init__(self):
        self.circle = Circle()
        self.rectangle = Rectangle()

    def drawCircle(self):
        self.circle.draw()
    def drawRectangle(self):
        self.rectangle.draw()

sm = ShapeMaker()
sm.drawCircle()
sm.drawRectangle()