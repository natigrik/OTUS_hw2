from src.Figure import Figure


class Rectangle(Figure):
    name = "rectangle"

    def __init__(self, first_side, second_side):
        if first_side <= 0 or second_side <= 0:
            raise ValueError("Both sides must be >0!")
        self.first_side = first_side
        self.second_side = second_side

    @property
    def area(self):
        s = round(self.first_side * self.second_side, 2)
        return s

    @property
    def perimeter(self):
        per = round((self.first_side + self.second_side) * 2, 2)
        return per
