import pytest

from vectorzz import Vec3, Scene
from vectorzz import Vec2
from vectorzz import cross
from vectorzz import dot
from vectorzz import parallelogram_area
from vectorzz import scalar_projection
from vectorzz import angle_between_deg
from vectorzz import DifferentDimensionException
from vectorzz import Line3
from vectorzz import P3
from vectorzz import Plane
from vectorzz import is_scalar_multiple
from vectorzz import Intersection
from vectorzz import XY_PLANE, ZX_PLANE, YZ_PLANE
from vectorzz import ShortestDistance


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


def test_initialize_point3():
    p = P3(1, 2, 3)
    assert str(p) == "P3(1, 2, 3)"
    p = P3(-1, -2, -3)
    assert str(p) == "P3(-1, -2, -3)"
    p = P3(0, 0, 0)
    assert str(p) == "P3(0, 0, 0)"
    p = P3(0.5, 1.0, 1.5)
    assert str(p) == "P3(0.5, 1.0, 1.5)"
    p = P3(-0.5, -1.0, -1.5)
    assert str(p) == "P3(-0.5, -1.0, -1.5)"


def test_subtract_point3():
    p1 = P3(1, 2, 3)
    p2 = P3(4, 5, 6)
    print(p1 - p2)
    assert p1 - p2 == P3(-3, -3, -3)
    assert p2 - p1 == P3(3, 3, 3)
    p1 = P3(-1, -2, -3)
    p2 = P3(-4, -5, -6)
    assert p1 - p2 == P3(3, 3, 3)
    assert p2 - p1 == P3(-3, -3, -3)
    p1 = P3(0.5, 1.0, 1.5)
    p2 = P3(1.0, 1.5, 2.0)
    assert p1 - p2 == P3(-0.5, -0.5, -0.5)
    assert p2 - p1 == P3(0.5, 0.5, 0.5)


def test_add_points3():
    p1 = P3(1, 2, 3)
    p2 = P3(4, 5, 6)
    assert p1 + p2 == P3(5, 7, 9)
    p1 = P3(-1, -2, -3)
    p2 = P3(-4, -5, -6)
    assert p1 + p2 == P3(-5, -7, -9)
    p1 = P3(0.5, 1.0, 1.5)
    p2 = P3(1.0, 1.5, 2.0)
    assert p1 + p2 == P3(1.5, 2.5, 3.5)


def test_point3_to_vec3():
    p1 = P3(1, 2, 3)
    assert p1.to_vec3() == Vec3(1, 2, 3)
    p1 = P3(-1, -2, -3)
    assert p1.to_vec3() == Vec3(-1, -2, -3)
    p1 = P3(0.5, 1.0, 1.5)
    assert p1.to_vec3() == Vec3(0.5, 1.0, 1.5)


def test_initialize_line3():
    with pytest.raises(ValueError):
        Line3(P3(1, 2, 3), Vec2(1, 2))
    line = Line3(Vec3(1, 2, 3), Vec3(4, 5, 6))
    assert str(line) == "Line3(Vec3(1, 2, 3), Vec3(4, 5, 6))"
    line = Line3.from_points(P3(1, 2, 3), P3(4, 5, 6))
    assert str(line) == "Line3(Vec3(1, 2, 3), Vec3(3, 3, 3))"


def test_line3_is_parallel():
    line1 = Line3(Vec3(1, 2, 3), Vec3(4, 5, 6))
    line2 = Line3(Vec3(6, 7, 8), Vec3(4, 5, 6))
    assert line1.is_parallel(line2)
    line1 = Line3(Vec3(1, 2, 3), Vec3(4, 5, 6))
    line2 = Line3(Vec3(6, 7, 8), Vec3(8, 10, 12))
    assert line1.is_parallel(line2)
    line1 = Line3(Vec3(1, 2, 3), Vec3(4, 5, 6))
    line2 = Line3(Vec3(6, 7, 8), Vec3(4, 5, 7))
    assert not line1.is_parallel(line2)
    line1 = Line3(Vec3(1, 2, 3), Vec3(-1, -2, 5))
    line2 = Line3(Vec3(6, 7, 8), Vec3(-0.5, -1, 2.5))
    assert line1.is_parallel(line2)
    line1 = Line3(Vec3(1, 2, 3), Vec3(-1, -2, 5))
    line2 = Line3(Vec3(6, 7, 8), Vec3(-0.5, -1, 2.6))
    assert not line1.is_parallel(line2)


def test_line3_contains_point():
    line = Line3(Vec3(1, 2, 3), Vec3(4, 5, 6))
    assert line.contains_point(P3(1, 2, 3))
    assert line.contains_point(P3(9, 12, 15))
    assert line.contains_point(P3(3, 4.5, 6))
    assert not line.contains_point(P3(4, 5, 6))
    assert not line.contains_point(P3(2.6, 3.5, 4.5))
    assert not line.contains_point(P3(2.5, 3.6, 4.5))
    assert not line.contains_point(P3(2.5, 3.5, 4.6))
    assert not line.contains_point(P3(2.4, 3.5, 4.5))
    assert not line.contains_point(P3(2.5, 3.4, 4.5))
    assert not line.contains_point(P3(2.5, 3.5, 4.4))
    assert not line.contains_point(P3(1, 2, 4))
    assert not line.contains_point(P3(1, 2, 2))
    assert not line.contains_point(P3(1, 3, 3))
    assert not line.contains_point(P3(1, 1, 3))
    assert not line.contains_point(P3(0, 2, 3))
    assert not line.contains_point(P3(2, 2, 3))


def test_vec3_to_point():
    v = Vec3(1, 2, 3)
    assert v.to_point() == P3(1, 2, 3)
    v = Vec3(-1, -2, -3)
    assert v.to_point() == P3(-1, -2, -3)
    v = Vec3(0.5, 1.0, 1.5)
    assert v.to_point() == P3(0.5, 1.0, 1.5)


def test_line3_equals():
    line1 = Line3(Vec3(1, 2, 3), Vec3(4, 5, 6))
    assert line1 == line1
    assert line1 == Line3(Vec3(1, 2, 3), Vec3(8, 10, 12))
    assert line1 == Line3(Vec3(5, 7, 9), Vec3(8, 10, 12))
    assert line1 == Line3(Vec3(-1, -0.5, 0), Vec3(2, 2.5, 3))
    assert line1 != Line3(Vec3(1, 2, 3), Vec3(4, 5, 7))
    assert line1 != Line3(Vec3(1, 2, 3), Vec3(4, 6, 6))
    assert line1 != Line3(Vec3(2.25, 2, 3), Vec3(4, 5, 6))


def test_str_vec3():
    v = Vec3(1, 2, 3)
    assert str(v) == "Vec3(1, 2, 3)"

    v = Vec3(-1, -2, -3)
    assert str(v) == "Vec3(-1, -2, -3)"

    v = Vec3(0, 0, 0)
    assert str(v) == "Vec3(0, 0, 0)"

    v = Vec3(1.5, 2.5, 3.5)
    assert str(v) == "Vec3(1.5, 2.5, 3.5)"

    v = Vec3(-1.5, -2.5, -3.5)
    assert str(v) == "Vec3(-1.5, -2.5, -3.5)"


def test_str_vec2():
    v = Vec2(1, 2)
    assert str(v) == "Vec2(1, 2)"

    v = Vec2(-1, -2)
    assert str(v) == "Vec2(-1, -2)"

    v = Vec2(0, 0)
    assert str(v) == "Vec2(0, 0)"

    v = Vec2(1.5, 2.5)
    assert str(v) == "Vec2(1.5, 2.5)"

    v = Vec2(-1.5, -2.5)
    assert str(v) == "Vec2(-1.5, -2.5)"


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


def test_initialize_plane():
    p1 = Plane(P3(4, 5, 6,), Vec3(1, 2, 3))
    assert str(p1) == "Plane(P3(4, 5, 6), Vec3(1, 2, 3))"


def test_plane_d():
    p1 = Plane(P3(4, 5, 6), Vec3(1, 2, 3))
    assert p1.d == -32
    p2 = Plane(P3(0, 0, 0), Vec3(0, 0, 0))
    assert p2.d == 0


def test_plane_contains_point():
    p1 = Plane(P3(4, 5, 6), Vec3(1, 2, 3))
    assert p1.contains_point(P3(4, 5, 6))
    assert p1.contains_point(P3(0, 0, 32/3))
    assert not p1.contains_point(P3(0, 0, 0))


def test_plane_eq():
    p1 = Plane(P3(4, 5, 6), Vec3(1, 2, 3))
    p2 = Plane(P3(4, 5, 6), Vec3(1, 2, 3))
    assert p1 == p2
    p3 = Plane(P3(4, 5, 6), Vec3(2, 4, 6))
    assert p1 == p3
    p4 = Plane(P3(0, 0, 32/3), Vec3(1, 2, 3))
    assert p1 == p4
    p4 = Plane(P3(0, 0, 33 / 3), Vec3(1, 2, 3))
    assert p1 != p4


def test_is_scalar_multiple():
    assert is_scalar_multiple(Vec3(1, 2, 3), Vec3(2, 4, 6))
    assert is_scalar_multiple(Vec3(145, 92, 33), Vec3(145/7, 92/7, 33/7))
    assert not is_scalar_multiple(Vec3(1, 2, 3), Vec3(2, 4, 7))

    with pytest.raises(ValueError):
        is_scalar_multiple(Vec3(1, 2, 3), Vec2(2, 4))
    with pytest.raises(ValueError):
        is_scalar_multiple(P3(1, 2, 3), Vec3(2, 4, 7))


def test_plane_is_parallel():
    p1 = Plane(P3(4, 5, 6), Vec3(1, 2, 3))
    assert p1.is_parallel(Plane(P3(4, 5, 6), Vec3(1, 2, 3)))
    assert p1.is_parallel(Plane(P3(4, 5, 6), Vec3(2, 4, 6)))
    assert p1.is_parallel(Plane(P3(0, 0, 32/3), Vec3(1, 2, 3)))
    assert p1.is_parallel(Plane(P3(0, 0, 33/3), Vec3(1, 2, 3)))
    assert not p1.is_parallel(Plane(P3(0, 0, 0), Vec3(1, 2, 42)))

    p2 = Plane.from_normal_and_d(Vec3(1, 1, 1), -2)
    line = Line3(Vec3(0, 0, 0), Vec3(0, 2, 0))
    assert not p2.is_parallel(line)

    line = Line3(Vec3(0, 0, 0), Vec3(0, 0, 1))
    assert ZX_PLANE.is_parallel(line)

    with pytest.raises(ValueError):
        p1.is_parallel(Vec2(1, 2))


def test_point_at_t():
    l1 = Line3(Vec3(1, 2, 3), Vec3(4, 5, 6))
    assert l1.point_at_t(0) == P3(1, 2, 3)
    assert l1.point_at_t(1) == P3(5, 7, 9)


def test_line_plane_intersection():
    plane = Plane.from_normal_and_d(Vec3(3, -2, 1), -10)
    line = Line3(Vec3(2, 1, 0), Vec3(-1, 1, 3))
    intersection = Intersection.line_plane(line, plane)
    assert intersection == P3(5, -2, -9)

    line = Line3(Vec3(0, 0, 1), Vec3(0, 0, 2))
    assert Intersection.line_plane(line, XY_PLANE) == P3(0, 0, 0)

    line = Line3(Vec3(0, 1, 0), Vec3(0, 2, 0))
    assert Intersection.line_plane(line, ZX_PLANE) == P3(0, 0, 0)

    line = Line3(Vec3(1, 0, 0), Vec3(1, 0, 0))
    assert Intersection.line_plane(line, YZ_PLANE) == P3(0, 0, 0)

    line = Line3(Vec3(0, 0, 0), Vec3(0, 0, 1))
    assert Intersection.line_plane(line, YZ_PLANE) == line

    line = Line3(Vec3(1, 1, 1), Vec3(0, 1, 0))
    assert Intersection.line_plane(line, YZ_PLANE) is None


def test_shortest_distance_point_point():
    p1 = P3(1, 2, 3)
    p2 = P3(4, 5, 6)
    assert ShortestDistance.point_point(p1, p2) == 5.196152422706632

    p1 = P3(1, 2, 3)
    p2 = P3(1, 2, 3)
    assert ShortestDistance.point_point(p1, p2) == 0

    p1 = P3(0, 0, 1)
    p2 = P3(0, 0, 0)
    assert ShortestDistance.point_point(p1, p2) == 1


def test_shortest_distance_line_line():
    pass


def test_shortest_distance_line_plane():
    pass


def test_shortest_distance_plane_plane():
    pass


def test_shortest_distance_point_line():
    pass


def test_shortest_distance_point_plane():
    pass


def test_init_scene():
    scene = Scene()
    assert not bool(scene.vectors)
    assert not bool(scene.points)
    assert not bool(scene.lines)
    assert scene.fig is None


def test_add_vector():
    scene = Scene()
    v1 = Vec3(1, 2, 3)
    scene.add(v1)
    assert v1 in scene.vectors


def test_add_point():
    scene = Scene()
    p1 = P3(1, 2, 3)
    scene.add(p1)
    assert p1 in scene.points


def test_add_line():
    scene = Scene()
    line = Line3(Vec3(1, 2, 3), Vec3(4, 5, 6))
    scene.add(line)
    assert line in scene.lines


def test_add_invalid():
    scene = Scene()
    with pytest.raises(ValueError):
        scene.add(Vec2(1, 2))


def test_add_many():
    scene = Scene()
    v1 = Vec3(1, 2, 3)
    p1 = P3(1, 2, 3)
    line = Line3(Vec3(1, 2, 3), Vec3(4, 5, 6))
    scene.add(v1, p1, line)
    assert v1 in scene.vectors
    assert p1 in scene.points
    assert line in scene.lines


def test_draw_scene():
    scene = Scene()
    v1 = Vec3(1, 2, 3)
    p1 = P3(1, 2, 3)
    line = Line3(Vec3(1, 2, 3), Vec3(4, 5, 6))
    scene.add(v1, p1, line)
    scene.draw(show=False)
    assert True
