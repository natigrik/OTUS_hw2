from src.Circle import Circle
import pytest
import math


def test_create_circle(circle):
    assert circle


@pytest.mark.parametrize("radius", [0, -1, -10.556])
def test_create_fail_circle(radius):
    with pytest.raises(ValueError):
        Circle(radius)


@pytest.mark.parametrize("attribute", ["name", "area", "perimeter"])
def test_circle_has_attribute(circle, attribute):
    assert hasattr(circle, attribute)


def test_circle_area(circle):
    s = round((circle.radius ** 2) * math.pi, 2)
    assert circle.area == s


def test_circle_perimeter(circle):
    per = round(circle.radius * 2 * math.pi, 2)
    assert circle.perimeter == per


def test_circle_add_area_rectangle(circle, rectangle):
    assert circle.add_area(rectangle) == circle.area + rectangle.area


def test_circle_add_area_triangle(circle, triangle):
    assert circle.add_area(triangle) == circle.area + triangle.area


def test_circle_add_area_square(circle, square):
    assert circle.add_area(square) == circle.area + square.area


def test_circle_add_area_not_figure(circle, not_figure):
    with pytest.raises(ValueError):
        circle.add_area(not_figure)
