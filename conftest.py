import pytest

from src.Figure import Figure
from src.Square import Square
from src.Circle import Circle
from src.Rectangle import Rectangle
from src.Triangle import Triangle


class NotFigure(object):
    name = "not_figure"
    area = 0
    perimeter = 0


# создание объектов с валидными параметрами
@pytest.fixture(scope="session", params=[[20, 35, 30], [3, 4, 5], [9, 9, 9], [3.50, 4.335, 5.58]])
def triangle(request):
    return Triangle(request.param[0], request.param[1], request.param[2])


@pytest.fixture(scope="session", params=[[5, 10], [2.5, 3.65], [403, 403]])
def rectangle(request):
    return Rectangle(request.param[0], request.param[1])


@pytest.fixture(scope="session", params=[10, 55.55])
def square(request):
    return Square(request.param)


@pytest.fixture(scope="session", params=[550, 3.336])
def circle(request):
    return Circle(request.param)


# создание объекта, не относящегося к классу Figure
@pytest.fixture(scope="session")
def not_figure():
    return NotFigure()
