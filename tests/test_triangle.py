from src.Triangle import Triangle
import pytest
import math


def test_create_triangle(triangle):
    assert triangle


@pytest.mark.parametrize("first_side", [0, -2, 50])
def test_fail_first_side_triangle(first_side):
    with pytest.raises(ValueError):
        triangle = Triangle(first_side, 4, 5)


@pytest.mark.parametrize("second_side", [0, -3, 33])
def test_fail_second_side_triangle(second_side):
    with pytest.raises(ValueError):
        triangle = Triangle(3, second_side, 5)


@pytest.mark.parametrize("third_side", [0, -5, 1000])
def test_fail_third_side_triangle(third_side):
    with pytest.raises(ValueError):
        triangle = Triangle(3, 4, third_side)


@pytest.mark.parametrize("attribute", ["name", "area", "perimeter"])
def test_triangle_has_attribute(triangle, attribute):
    assert hasattr(triangle, attribute)


def test_triangle_area(triangle):
    p = (triangle.first_side + triangle.second_side + triangle.third_side) / 2
    s = math.sqrt(p * (p - triangle.first_side) * (p - triangle.second_side) * (p - triangle.third_side))
    assert triangle.area == s.__round__(2)


def test_triangle_perimeter(triangle):
    per = triangle.first_side + triangle.second_side + triangle.third_side
    assert triangle.perimeter == per.__round__(2)


def test_triangle_add_area_square(triangle, square):
    assert triangle.add_area(square) == triangle.area + square.area


def test_triangle_add_area_rectangle(triangle, rectangle):
    assert triangle.add_area(rectangle) == triangle.area + rectangle.area


def test_triangle_add_area_circle(triangle, circle):
    assert triangle.add_area(circle) == triangle.area + circle.area


def test_triangle_add_area_other(triangle, other):
    with pytest.raises(ValueError):
        triangle.add_area(other)
