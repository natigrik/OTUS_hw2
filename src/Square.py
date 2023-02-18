from src.Rectangle import Rectangle


class Square(Rectangle):
    name = "square"

    def __init__(self, side):
        if side <= 0:
            raise ValueError("Side must be >0!")
        first_side = side
        second_side = side
        super().__init__(first_side, second_side)
        self.side = side
