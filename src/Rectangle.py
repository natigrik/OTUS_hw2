from src.Figure import Figure


class Rectangle(Figure):
    name = "rectangle"

    def __init__(self, first_side, second_side):
        if first_side <= 0:
            raise ValueError("First side must be >0!")
        elif second_side <= 0:
            raise ValueError("Second side must be >0!")
        elif first_side == second_side:
            raise ValueError("This figure is square, not rectangle!")
        else:
            self.first_side = first_side
            self.second_side = second_side

    @property
    def area(self):
        s = self.first_side * self.second_side
        return s.__round__(2)

    @property
    def perimeter(self):
        per = (self.first_side + self.second_side) * 2
        return per.__round__(2)
