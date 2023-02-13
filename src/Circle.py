from src.Figure import Figure
import math


class Circle(Figure):
    name = "circle"

    def __init__(self, radius):
        if radius <= 0:
            raise ValueError("Radius must be >0!")
        else:
            self.radius = radius
        self.radius = radius

    @property
    def area(self):
        s = (self.radius ** 2) * math.pi
        return s.__round__(2)

    @property
    def perimeter(self):
        per = self.radius * 2 * math.pi
        return per.__round__(2)
