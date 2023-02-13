from src.Figure import Figure


class Square(Figure):
    name = "square"

    def __init__(self, side):
        if side <= 0:
            raise ValueError("Side must be >0!")
        else:
            self.side = side

    @property
    def area(self):
        s = self.side ** 2
        return s.__round__(2)

    @property
    def perimeter(self):
        per = self.side * 4
        return per.__round__(2)
