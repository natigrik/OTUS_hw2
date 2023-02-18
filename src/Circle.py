from src.Figure import Figure
import math


class Circle(Figure):
    name = "circle"

    def __init__(self, radius):
        if radius <= 0:
            raise ValueError("Radius must be >0!")
        self.radius = radius

    @property
    def area(self):
        s = round((self.radius ** 2) * math.pi, 2)
        return s

    @property
    def perimeter(self):
        per = round(self.radius * 2 * math.pi, 2)
        return per
