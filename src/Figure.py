class Figure(object):
    name = "figure"
    area = 0
    perimeter = 0
    figures = ['triangle', 'rectangle', 'circle', 'square']

    def add_area(self, figure):
        if figure.name in self.figures:
            return self.area + figure.area
        else:
            raise ValueError('Wrong figure: ' + str(figure.name))
