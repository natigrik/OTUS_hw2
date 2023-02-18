from src.Square import Square
import pytest


def test_create_square(square):
    assert square


@pytest.mark.parametrize("side", [0, -4, -14.50])
def test_create_fail_square(side):
    with pytest.raises(ValueError):
        Square(side)


@pytest.mark.parametrize("attribute", ["name", "area", "perimeter"])
def test_circle_has_attribute(square, attribute):
    assert hasattr(square, attribute)


def test_square_area(square):
    s = round(square.side ** 2, 2)
    assert square.area == s


def test_square_perimeter(square):
    per = round(square.side * 4, 2)
    assert square.perimeter == per


def test_square_add_area_rectangle(square, rectangle):
    assert square.add_area(rectangle) == square.area + rectangle.area


def test_square_add_area_triangle(square, triangle):
    assert square.add_area(triangle) == square.area + triangle.area


def test_square_add_area_circle(square, circle):
    assert square.add_area(circle) == square.area + circle.area


def test_square_add_area_not_figure(square, not_figure):
    with pytest.raises(ValueError):
        square.add_area(not_figure)
