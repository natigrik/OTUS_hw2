from src.Rectangle import Rectangle
import pytest


def test_create_rectangle(rectangle):
    assert rectangle


@pytest.mark.parametrize("first_side, second_side", [(0, 0), (0, 100), (67.7, 0), (-11, 7), (5, -15.5), (-12, -3.33)])
def test_create_fail_rectangle(first_side, second_side):
    with pytest.raises(ValueError):
        Rectangle(first_side, second_side)


@pytest.mark.parametrize("attribute", ["name", "area", "perimeter"])
def test_rectangle_has_attribute(rectangle, attribute):
    assert hasattr(rectangle, attribute)


def test_rectangle_area(rectangle):
    s = round(rectangle.first_side * rectangle.second_side, 2)
    assert rectangle.area == s


def test_rectangle_perimeter(rectangle):
    per = round((rectangle.first_side + rectangle.second_side) * 2, 2)
    assert rectangle.perimeter == per


def test_rectangle_add_area_square(rectangle, square):
    assert rectangle.add_area(square) == rectangle.area + square.area


def test_rectangle_add_area_triangle(rectangle, triangle):
    assert rectangle.add_area(triangle) == rectangle.area + triangle.area


def test_rectangle_add_area_circle(rectangle, circle):
    assert rectangle.add_area(circle) == rectangle.area + circle.area


def test_rectangle_add_area_not_figure(rectangle, not_figure):
    with pytest.raises(ValueError):
        rectangle.add_area(not_figure)
