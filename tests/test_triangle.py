from src.Triangle import Triangle
import pytest
import math


def test_create_triangle(triangle):
    assert triangle


@pytest.mark.parametrize("first_side, second_side, third_side", [(0, 2, 3), (1, 0, 3), (1, 2, 0),
                                                                 (0, 0, 1), (0, 0, 0),
                                                                 (-1, 2, 3), (1, -2, 3), (1, 2, -3),
                                                                 (-1, -2, 3), (-1, -2, -3),
                                                                 (1000, 23.33, 54), (13.9, 505, 44), (5, 7, 66.6)])
def test_create_fail_triangle(first_side, second_side, third_side):
    with pytest.raises(ValueError):
        Triangle(first_side, second_side, third_side)


@pytest.mark.parametrize("attribute", ["name", "area", "perimeter"])
def test_triangle_has_attribute(triangle, attribute):
    assert hasattr(triangle, attribute)


def test_triangle_area(triangle):
    p = (triangle.first_side + triangle.second_side + triangle.third_side) / 2
    s = round(math.sqrt(p * (p - triangle.first_side) * (p - triangle.second_side) * (p - triangle.third_side)), 2)
    assert triangle.area == s


def test_triangle_perimeter(triangle):
    per = round(triangle.first_side + triangle.second_side + triangle.third_side, 2)
    assert triangle.perimeter == per


def test_triangle_add_area_square(triangle, square):
    assert triangle.add_area(square) == triangle.area + square.area


def test_triangle_add_area_rectangle(triangle, rectangle):
    assert triangle.add_area(rectangle) == triangle.area + rectangle.area


def test_triangle_add_area_circle(triangle, circle):
    assert triangle.add_area(circle) == triangle.area + circle.area


def test_triangle_add_area_not_figure(triangle, not_figure):
    with pytest.raises(ValueError):
        triangle.add_area(not_figure)
