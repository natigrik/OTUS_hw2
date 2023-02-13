from src.Rectangle import Rectangle
import pytest


def test_create_rectangle(rectangle):
    assert rectangle


@pytest.mark.parametrize("first_side", [0, -4, 1])
def test_fail_first_side_rectangle(first_side):
    with pytest.raises(ValueError):
        rectangle = Rectangle(first_side, 1)


@pytest.mark.parametrize("second_side", [0, -1, 1])
def test_fail_second_side_rectangle(second_side):
    with pytest.raises(ValueError):
        rectangle = Rectangle(1, second_side)


@pytest.mark.parametrize("attribute", ["name", "area", "perimeter"])
def test_rectangle_has_attribute(rectangle, attribute):
    assert hasattr(rectangle, attribute)


def test_rectangle_area(rectangle):
    s = rectangle.first_side * rectangle.second_side
    assert rectangle.area == s.__round__(2)


def test_rectangle_perimeter(rectangle):
    per = (rectangle.first_side + rectangle.second_side) * 2
    assert rectangle.perimeter == per.__round__(2)


def test_rectangle_add_area_square(rectangle, square):
    assert rectangle.add_area(square) == rectangle.area + square.area


def test_rectangle_add_area_triangle(rectangle, triangle):
    assert rectangle.add_area(triangle) == rectangle.area + triangle.area


def test_rectangle_add_area_circle(rectangle, circle):
    assert rectangle.add_area(circle) == rectangle.area + circle.area


def test_rectangle_add_area_other(rectangle, other):
    with pytest.raises(ValueError):
        rectangle.add_area(other)
