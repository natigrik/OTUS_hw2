import pytest

from src.Figure import Figure
from src.Square import Square
from src.Circle import Circle
from src.Rectangle import Rectangle
from src.Triangle import Triangle


# создание объектов с валидными параметрами
@pytest.fixture(scope="session", params=[[2, 3, 4], [3, 4, 5], [9, 9, 9], [3.5, 4.5, 5.5]])
def triangle(request):
    return Triangle(request.param[0], request.param[1], request.param[2])


@pytest.fixture(scope="session", params=[[5, 10], [2.5, 3.65]])
def rectangle(request):
    return Rectangle(request.param[0], request.param[1])


@pytest.fixture(scope="session", params=[10, 55.55])
def square(request):
    return Square(request.param)


@pytest.fixture(scope="session", params=[3, 7.7])
def circle(request):
    return Circle(request.param)


# создание объекта, не относящегося к классу Figure
@pytest.fixture(scope="session")
def other():
    other.name = 'other'
    other.area = 0
    other.perimeter = 0
    return other
