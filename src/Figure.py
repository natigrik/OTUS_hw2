class Figure(object):
    name = None
    area = None
    perimeter = None
    figures = ['triangle', 'rectangle', 'circle', 'square']

    def add_area(self, figure):
        if figure.name in Figure.figures:
            return self.area + figure.area
        else:
            raise ValueError('Wrong figure name!')
