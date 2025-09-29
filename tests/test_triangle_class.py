import pytest
from geometric_calculator import Triangle


def test_triangle_area():
    triangle = Triangle(3.0, 4.0, 5.0)
    expected_area = 6.0

    actual_area = triangle.area

    assert actual_area == pytest.approx(expected_area)


def test_triangle_perimetr():
    triangle = Triangle(3.0, 4.0, 5.0)
    expected_perimeter = 12.0

    actual_perimeter = triangle.perimeter

    assert actual_perimeter == pytest.approx(expected_perimeter)


def test_is_triangle_with_negative_side():
    side_1 = -1.0
    side_2 = 2.0
    side_3 = 2.0

    with pytest.raises(ValueError):
        Triangle(side_1, side_2, side_3)


def test_triangle_area_with_small_valid_sides():
    triangle = Triangle(0.001, 0.001, 0.001)
    area = triangle.area
    assert isinstance(area, float)
    assert area > 0


def test_triangle_with_degenerate_sides():
    side_1, side_2, side_3 = 1.0, 2.0, 3.0

    with pytest.raises(ValueError):
        Triangle(side_1, side_2, side_3)

