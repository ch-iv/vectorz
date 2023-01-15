import pytest

from vectorzz import Vec3
from vectorzz import Vec2
from vectorzz import cross
from vectorzz import dot
from vectorzz import parallelogram_area
from vectorzz import scalar_projection
from vectorzz import angle_between_deg
from vectorzz import DifferentDimensionException


def test_initialize_vec3():
    v = Vec3(1, 2, 3)
    assert v.x == 1
    assert v.y == 2
    assert v.z == 3

    v = Vec3(-1, -2, -3)
    assert v.x == -1
    assert v.y == -2
    assert v.z == -3

    v = Vec3(0, 0, 0)
    assert v.x == 0
    assert v.y == 0
    assert v.z == 0

    v = Vec3(1.5, 2.5, 3.5)
    assert v.x == 1.5
    assert v.y == 2.5
    assert v.z == 3.5

    v = Vec3(-1.5, -2.5, -3.5)
    assert v.x == -1.5
    assert v.y == -2.5
    assert v.z == -3.5


def test_initialize_vec2():
    v = Vec2(1, 2)
    assert v.x == 1
    assert v.y == 2

    v = Vec2(-1, -2)
    assert v.x == -1
    assert v.y == -2

    v = Vec2(0, 0)
    assert v.x == 0
    assert v.y == 0

    v = Vec2(1.5, 2.5)
    assert v.x == 1.5
    assert v.y == 2.5

    v = Vec2(-1.5, -2.5)
    assert v.x == -1.5
    assert v.y == -2.5


def test_str_vec3():
    v = Vec3(1, 2, 3)
    assert str(v) == "(1, 2, 3)"

    v = Vec3(-1, -2, -3)
    assert str(v) == "(-1, -2, -3)"

    v = Vec3(0, 0, 0)
    assert str(v) == "(0, 0, 0)"

    v = Vec3(1.5, 2.5, 3.5)
    assert str(v) == "(1.5, 2.5, 3.5)"

    v = Vec3(-1.5, -2.5, -3.5)
    assert str(v) == "(-1.5, -2.5, -3.5)"


def test_str_vec2():
    v = Vec2(1, 2)
    assert str(v) == "(1, 2)"

    v = Vec2(-1, -2)
    assert str(v) == "(-1, -2)"

    v = Vec2(0, 0)
    assert str(v) == "(0, 0)"

    v = Vec2(1.5, 2.5)
    assert str(v) == "(1.5, 2.5)"

    v = Vec2(-1.5, -2.5)
    assert str(v) == "(-1.5, -2.5)"


def test_magnitude_vec3():
    v = Vec3(1, 2, 3)
    assert v.magnitude() == 3.7416573867739413

    v = Vec3(-1, -2, -3)
    assert v.magnitude() == 3.7416573867739413

    v = Vec3(0, 0, 0)
    assert v.magnitude() == 0

    v = Vec3(1.5, 2.5, 3.5)

    assert v.magnitude() == 4.55521678957215

    v = Vec3(-1.5, -2.5, -3.5)
    assert v.magnitude() == 4.55521678957215


def test_magnitude_vec2():
    v = Vec2(1, 2)
    assert v.magnitude() == 2.23606797749979

    v = Vec2(-1, -2)
    assert v.magnitude() == 2.23606797749979

    v = Vec2(0, 0)
    assert v.magnitude() == 0

    v = Vec2(1.5, 2.5)
    assert v.magnitude() == 2.9154759474226504

    v = Vec2(-1.5, -2.5)
    assert v.magnitude() == 2.9154759474226504


def test_multiplication_by_scalar():
    v = Vec3(1, 2, 3)
    assert v * 2 == Vec3(2, 4, 6)
    assert v * 0 == Vec3(0, 0, 0)
    assert v * -1 == Vec3(-1, -2, -3)
    assert v * 2.5 == Vec3(2.5, 5, 7.5)
    assert v * -2.5 == Vec3(-2.5, -5, -7.5)

    v = Vec2(1, 2)
    assert v * 2 == Vec2(2, 4)
    assert v * 0 == Vec2(0, 0)
    assert v * -1 == Vec2(-1, -2)
    assert v * 2.5 == Vec2(2.5, 5)
    assert v * -2.5 == Vec2(-2.5, -5)


def test_division_by_scalar():
    v = Vec3(1, 2, 3)
    assert v / 2 == Vec3(0.5, 1, 1.5)
    assert v / 1 == Vec3(1, 2, 3)
    assert v / -1 == Vec3(-1, -2, -3)
    assert v / 2.5 == Vec3(0.4, 0.8, 1.2)
    assert v / -2.5 == Vec3(-0.4, -0.8, -1.2)

    v = Vec2(1, 2)
    assert v / 2 == Vec2(0.5, 1)
    assert v / 1 == Vec2(1, 2)
    assert v / -1 == Vec2(-1, -2)
    assert v / 2.5 == Vec2(0.4, 0.8)
    assert v / -2.5 == Vec2(-0.4, -0.8)


def test_addition():
    v1 = Vec3(1, 2, 3)
    v2 = Vec3(4, 5, 6)
    v3 = Vec3(1, 2, 3)
    v4 = Vec3(-1, -2, -3)
    v5 = Vec3(0.5, 1.5, 2.5)

    assert v1 + v2 == Vec3(5, 7, 9)
    assert v2 + v1 == Vec3(5, 7, 9)
    assert v1 + v3 == Vec3(2, 4, 6)
    assert v1 + v4 == Vec3(0, 0, 0)
    assert v1 + v5 == Vec3(1.5, 3.5, 5.5)

    v1 = Vec2(1, 2)
    v2 = Vec2(4, 5)
    v3 = Vec2(1, 2)
    v4 = Vec2(-1, -2)
    v5 = Vec2(0.5, 1.5)

    assert v1 + v2 == Vec2(5, 7)
    assert v2 + v1 == Vec2(5, 7)
    assert v1 + v3 == Vec2(2, 4)
    assert v1 + v4 == Vec2(0, 0)
    assert v1 + v5 == Vec2(1.5, 3.5)


def test_subtraction():
    v1 = Vec3(1, 2, 3)
    v2 = Vec3(4, 5, 6)
    v3 = Vec3(1, 2, 3)
    v4 = Vec3(-1, -2, -3)
    v5 = Vec3(0.5, 1.5, 2.5)

    assert v1 - v2 == Vec3(-3, -3, -3)
    assert v2 - v1 == Vec3(3, 3, 3)
    assert v1 - v3 == Vec3(0, 0, 0)
    assert v1 - v4 == Vec3(2, 4, 6)
    assert v1 - v5 == Vec3(0.5, 0.5, 0.5)

    v1 = Vec2(1, 2)
    v2 = Vec2(4, 5)
    v3 = Vec2(1, 2)
    v4 = Vec2(-1, -2)
    v5 = Vec2(0.5, 1.5)

    assert v1 - v2 == Vec2(-3, -3)
    assert v2 - v1 == Vec2(3, 3)
    assert v1 - v3 == Vec2(0, 0)
    assert v1 - v4 == Vec2(2, 4)
    assert v1 - v5 == Vec2(0.5, 0.5)


def test_cross_product():
    v1 = Vec3(1, 2, 3)
    v2 = Vec3(4, 5, 6)
    v3 = Vec3(1, 2, 3)

    assert cross(v1, v2) == Vec3(-3, 6, -3)
    assert cross(v2, v1) == Vec3(3, -6, 3)
    assert cross(v1, v3) == Vec3(0, 0, 0)


def test_dot_product():
    v1 = Vec3(1, 2, 3)
    v2 = Vec3(4, 5, 6)
    v3 = Vec3(1, 2, 3)

    assert dot(v1, v2) == 32
    assert dot(v2, v1) == 32
    assert dot(v1, v3) == 14

    v1 = Vec2(1, 2)
    v2 = Vec2(4, 5)
    v3 = Vec2(1, 2)

    assert dot(v1, v2) == 14
    assert dot(v2, v1) == 14
    assert dot(v1, v3) == 5


def test_parallelogram_area():
    v1 = Vec3(1, 2, 3)
    v2 = Vec3(4, 5, 6)
    assert parallelogram_area(v1, v2) == Vec3(-3, 6, -3).magnitude()


def test_scalar_projection():
    v1 = Vec3(1, 2, 3)
    v2 = Vec3(4, 5, 6)
    assert scalar_projection(v1, v2) == 32 / v2.magnitude()


def test_angle_between_deg():
    v1 = Vec3(1, 2, 3)
    v2 = Vec3(2, 4, 6)
    assert angle_between_deg(v1, v2) == 0


def test_different_dimension_exception():
    v1 = Vec3(1, 2, 3)
    v2 = Vec2(1, 2)
    with pytest.raises(DifferentDimensionException):
        v1 + v2
    with pytest.raises(DifferentDimensionException):
        v2 + v1
    with pytest.raises(DifferentDimensionException):
        v1 - v2
    with pytest.raises(DifferentDimensionException):
        v2 - v1
    with pytest.raises(DifferentDimensionException):
        v1 == v2
    with pytest.raises(DifferentDimensionException):
        v2 == v1
    with pytest.raises(DifferentDimensionException):
        dot(v1, v2)
    with pytest.raises(DifferentDimensionException):
        scalar_projection(v1, v2)
    with pytest.raises(DifferentDimensionException):
        angle_between_deg(v1, v2)


def test_method_undefined_for_vec2():
    v1 = Vec2(1, 2)
    v2 = Vec2(1, 2)
    with pytest.raises(ValueError):
        cross(v1, v2)
    with pytest.raises(ValueError):
        parallelogram_area(v1, v2)
