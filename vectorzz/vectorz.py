"""This module provides a class for 2D and 3D vectors
 as well as utility functions for them"""
from __future__ import annotations

import math
from typing import Self
import matplotlib.pyplot as plt


class P3:
    """Represents a point in 3D space"""
    def __init__(self, x: int | float, y: int | float, z: int | float) -> None:
        self.x = x
        self.y = y
        self.z = z

    def __str__(self) -> str:
        """Return a string representation of the point"""
        return f"P3({self.x}, {self.y}, {self.z})"

    __repr__ = __str__

    def __sub__(self, other: Self) -> Self:
        """Subtract one point in 3D space from another"""
        return P3(self.x - other.x, self.y - other.y, self.z - other.z)

    def __add__(self, other: Self) -> Self:
        """Adds two 3D points together"""
        return P3(self.x + other.x, self.y + other.y, self.z + other.z)

    def __eq__(self, other) -> bool:
        """Check if two points are equal"""
        return self.x == other.x and self.y == other.y and self.z == other.z

    def to_vec3(self) -> Vec3:
        """Converts a point to a 3D vector from the origin to that point"""
        return Vec3(self.x, self.y, self.z)


class Vec3:
    """Represents a 3D vectors with x, y, z components"""
    def __init__(self,
                 x: int | float,
                 y: int | float,
                 z: int | float,) -> None:
        # the x component of the vector
        self.x = x
        # the y component of the vector
        self.y = y
        # the z component of the vector
        self.z = z

    def __str__(self):
        return f"Vec3({self.x}, {self.y}, {self.z})"

    __repr__ = __str__

    def __eq__(self, other: Self) -> bool:
        """Checks if two vectors are equal by checking
         if all of their components are equal"""
        if type(self) != type(other):
            raise DifferentDimensionException(self, other)
        return self.x == other.x and self.y == other.y and self.z == other.z

    def __add__(self, other: Self) -> Self:
        """Adds two vectors together"""
        if type(self) != type(other):
            raise DifferentDimensionException(self, other)
        return Vec3(self.x + other.x, self.y + other.y, self.z + other.z)

    def __sub__(self, other):
        """Subtracts two vectors"""
        if type(self) != type(other):
            raise DifferentDimensionException(self, other)
        return Vec3(self.x - other.x, self.y - other.y, self.z - other.z)

    def __mul__(self, other: int | float) -> Self:
        """Multiplies a vector by a scalar"""
        return Vec3(self.x * other, self.y * other, self.z * other)

    __rmul__ = __mul__

    def __truediv__(self, other: int | float):
        """Divides a vector by a scalar"""
        return Vec3(self.x / other, self.y / other, self.z / other)

    def magnitude(self) -> float | int:
        """Calculates the magnitude of the vector"""
        return math.sqrt(self.x**2 + self.y**2 + self.z**2)

    def to_point(self) -> P3:
        """Converts a vector to a point"""
        return P3(self.x, self.y, self.z)


class Vec2:
    """Represents a 2D vector with x and y components."""
    def __init__(self, x, y):
        # the x component of the vector
        self.x = x
        # the y component of the vector
        self.y = y

    def __str__(self):
        return f"Vec2({self.x}, {self.y})"

    __repr__ = __str__

    def __eq__(self, other) -> bool:
        """Checks if two vectors are equal by checking
         if all of their components are equal"""
        if type(self) != type(other):
            raise DifferentDimensionException(self, other)
        return self.x == other.x and self.y == other.y

    def __add__(self, other: Self) -> Self:
        """Adds two vectors together"""
        if type(self) != type(other):
            raise DifferentDimensionException(self, other)
        return Vec2(self.x + other.x, self.y + other.y)

    def __sub__(self, other: Self) -> Self:
        """Subtracts two vectors"""
        if type(self) != type(other):
            raise DifferentDimensionException(self, other)
        return Vec2(self.x - other.x, self.y - other.y)

    def __mul__(self, other: int | float) -> Self:
        """Multiplies a vector by a scalar"""
        return Vec2(self.x * other, self.y * other)

    __rmul__ = __mul__

    def __truediv__(self, other: int | float) -> Self:
        """Divides a vector by a scalar"""
        return Vec2(self.x / other, self.y / other)

    def magnitude(self):
        """Calculates the magnitude of the vector"""
        return math.sqrt(self.x**2 + self.y**2)


class Line3:
    """Represents a line in 3D space"""
    def __init__(self, origin_vector: Vec3, direction_vector: Vec3) -> None:
        if type(origin_vector) != Vec3 or type(direction_vector) != Vec3:
            raise ValueError(
                f"Expected type Vec3 for both arguments, got"
                f" {type(origin_vector)} and {type(direction_vector)} instead"
            )
        self.origin_vector: Vec3 = origin_vector
        self.direction_vector: Vec3 = direction_vector

    def is_parallel(self, other: Line3) -> bool:
        """Checks if two lines are parallel"""
        # check if the two direction vectors are multiples of each other
        try:
            coefficient_values = [
                self.direction_vector.x / other.direction_vector.x,
                self.direction_vector.y / other.direction_vector.y,
                self.direction_vector.z / other.direction_vector.z
            ]
            return len(set(coefficient_values)) == 1
        except ZeroDivisionError:
            # If a division by 0 error occurs, the lines are
            # only parallel if both direction vectors are the zero vector
            return self.direction_vector == other.direction_vector

    def contains_point(self, point: P3) -> bool:
        """Checks if a specific point is on the line"""
        # If a vector is in the form: r = origin_vec + t * direction_vec,
        # a point is on the line, if there exists a t such that
        # r = point
        try:
            # calculate t values for each component
            t_values = [
                (point.x - self.origin_vector.x) / self.direction_vector.x,
                (point.y - self.origin_vector.y) / self.direction_vector.y,
                (point.z - self.origin_vector.z) / self.direction_vector.z
            ]
            # the point is on the line if all t values are equal
            return len(set(t_values)) == 1
        except ZeroDivisionError:
            # If a division by 0 error occurs, the point is on the line if
            # the origin vector is the point
            return self.origin_vector.to_point() == point

    def __eq__(self, other: Line3) -> bool:
        """Checks if two lines are equal"""
        # Two lines are equal if they are parallel
        # and the origin vector of one is on the other
        return (
                self.is_parallel(other) and
                self.contains_point(other.origin_vector.to_point())
        )

    @staticmethod
    def from_points(p1: P3, p2: P3) -> Line3:
        """Creates a line from two points"""
        return Line3(p1.to_vec3(), (p2 - p1).to_vec3())

    def __str__(self) -> str:
        return f"Line3({self.origin_vector}, {self.direction_vector})"

    __repr__ = __str__

    def point_at_t(self, t: int | float) -> P3:
        """Calculates the point at a specific t value.
        t value is a scalar which multiplies the direction vector"""
        return (self.origin_vector + self.direction_vector * t).to_point()


class Plane:
    """
    Represents a plane in 3D space

    A plane in 3D space can be defined by:
    - 3 points on the plane
    - a point on the plane and a normal vector
    - 2 lines on the plane
    - a point and a line
    - a point and 2 direction vectors
    """
    def __init__(self, point: P3, normal: Vec3) -> None:
        """Creates a plane from a point and a normal vector"""
        self.point: P3 = point
        self.normal: Vec3 = normal
        # The equation of a plane is Ax + By + Cz + D = 0
        # where A, B, C are the components of the normal vector
        # and D is the negative dot product of the normal vector and the point
        self.d = -self.normal.x * self.point.x\
                 - self.normal.y * self.point.y\
                 - self.normal.z * self.point.z

    @staticmethod
    def from_normal_and_d(normal: Vec3, d: int | float) -> Plane:
        """Creates a plane from a normal vector and a d value"""
        return Plane(P3(0, 0, -d / normal.z), normal)

    def __str__(self) -> str:
        return f"Plane({self.point}, {self.normal})"

    __repr__ = __str__

    def __eq__(self, other: Plane) -> bool:
        """Checks if two planes are equal"""
        # Two planes are equal if they have the same normal vector
        # and the same D value
        return is_scalar_multiple(self.normal, other.normal)\
            and self.contains_point(other.point)

    def contains_point(self, point: P3) -> bool:
        """Checks if a point is on the plane"""
        return (
                self.normal.x * point.x
                + self.normal.y * point.y
                + self.normal.z * point.z + self.d
        ) == 0

    def is_parallel(self, other: Plane | Line3) -> bool:
        """Checks if two planes or a plane and a line are parallel"""
        if type(other) == Plane:
            return is_scalar_multiple(self.normal, other.normal)
        elif type(other) == Line3:
            return dot(self.normal, other.direction_vector) == 0
        else:
            raise ValueError(
                f"Expected type Plane or Line3, got {type(other)} instead"
            )


class DifferentDimensionException(Exception):
    """An error that is raised when two vectors have different dimensions"""
    def __init__(self, *args):
        message = f"Vectors {[v for v in args]} have different dimensions"
        super().__init__(message)


def cross(v1: Vec3, v2: Vec3) -> Vec3:
    """Calculates the cross product of two vectors.
    The cross product is only defined for 3D vectors"""

    if type(v1) == Vec3 and type(v2) == Vec3:
        return Vec3(
            v1.y * v2.z - v1.z * v2.y,
            v1.z * v2.x - v1.x * v2.z,
            v1.x * v2.y - v1.y * v2.x
        )
    else:
        # if v1 and v2 are not both 3D vectors, an error should be raised
        raise ValueError(
            "Cross product is only defined for 3D vectors of type Vec3"
        )


def dot(v1: Vec3 | Vec2, v2: Vec3 | Vec2) -> float | int:
    """Calculates the dot product of two vectors"""
    if type(v1) == Vec3 and type(v2) == Vec3:
        return v1.x * v2.x + v1.y * v2.y + v1.z * v2.z
    elif type(v1) == Vec2 and type(v2) == Vec2:
        return v1.x * v2.x + v1.y * v2.y
    else:
        # v1 and v2 must have the same dimension
        raise DifferentDimensionException(v1, v2)


def scalar_projection(v1: Vec3 | Vec2, v2: Vec3 | Vec2):
    """Scalar projection of v1 onto v2
     that is defined for both Vec3 and Vec2"""
    if type(v1) == type(v2):
        return dot(v1, v2) / v2.magnitude()
    raise DifferentDimensionException(v1, v2)


def angle_between_deg(v1: Vec3 | Vec2, v2: Vec3 | Vec2) -> float:
    """Angle between two vectors in degrees"""
    if type(v1) == type(v2):
        return math.degrees(
            math.acos(dot(v1, v2) / (v1.magnitude() * v2.magnitude()))
        )
    raise DifferentDimensionException(v1, v2)


def parallelogram_area(v1: Vec3, v2: Vec3) -> float | int:
    """Area of parallelogram spanned by two 3D vectors"""
    if type(v1) == Vec3 and type(v2) == Vec3:
        return cross(v1, v2).magnitude()
    else:
        raise ValueError(
            "Parallelogram area is only defined for 3D vectors of type Vec3"
        )


def is_scalar_multiple(v1: Vec3, v2: Vec3) -> bool:
    """Checks if two vectors are scalar multiples of each other"""
    if type(v1) == Vec3 and type(v2) == Vec3:
        return v1.x / v2.x == v1.y / v2.y == v1.z / v2.z
    else:
        raise ValueError(
            "Scalar multiple is only defined for 3D vectors of type Vec3"
        )


def neg(n: int | float) -> int | float:
    """Returns the negative of a number"""
    return -n


class ShortestDistance:
    @staticmethod
    def point_point(p1: P3, p2: P3):
        p1p2_vector = p1.to_vec3() - p2.to_vec3()
        return p1p2_vector.magnitude()

    @staticmethod
    def point_line(point: P3, line: Line3):
        pass

    @staticmethod
    def line_line(line1: Line3, line2: Line3):
        pass

    @staticmethod
    def point_plane(point: P3, plane: Plane):
        pass

    @staticmethod
    def line_plane(line: Line3, plane: Plane):
        pass

    @staticmethod
    def plane_plane(plane1: Plane, plane2: Plane):
        pass


class Intersection:
    @staticmethod
    def line_plane(line: Line3, plane: Plane) -> Line3 | P3 | None:
        """
        Calculate the intersection between a line and a plane
        A line and a plane can intersect in a line, when the line
        lies on the plane. A line and a plane do not intersect when
        the line is parallel to the plane. Otherwise, the line and
        the plane intersect in a single point.
        """
        try:
            t = (neg(plane.d) - dot(plane.normal, line.origin_vector)) \
                / dot(plane.normal, line.direction_vector)
        except ZeroDivisionError:
            t = 0
        point_on_line = line.point_at_t(t)

        if not plane.contains_point(point_on_line):
            # A point is not on the line
            return None
        if plane.is_parallel(line):
            # The line is on the plane
            return line
        # The line intersects the plane in a single point
        return point_on_line


# Axis dimensions for 3D drawing
DEFAULT_XLIM3D = (-10, 10)
DEFAULT_YLIM3D = (-10, 10)
DEFAULT_ZLIM3D = (-10, 10)

XY_PLANE = Plane(P3(0, 0, 0), Vec3(0, 0, 1))
YZ_PLANE = Plane(P3(0, 0, 0), Vec3(1, 0, 0))
ZX_PLANE = Plane(P3(0, 0, 0), Vec3(0, 1, 0))


class Scene:
    """A scene is used to store objects and display them"""
    def __init__(self) -> None:
        self.vectors: list[Vec3] = []
        self.points: list[P3] = []
        self.lines: list[Line3] = []
        self.fig = None

    def add(self, *args: Vec3 | P3 | Line3) -> None:
        """Adds objects to the scene"""
        for obj in args:
            if type(obj) == Vec3:
                self.vectors.append(obj)
            elif type(obj) == P3:
                self.points.append(obj)
            elif type(obj) == Line3:
                self.lines.append(obj)
            else:
                raise ValueError("Invalid object type")

    def draw(self, show=True) -> None:
        """Draws the scene"""
        fig = plt.figure()
        ax = fig.add_subplot(projection='3d')

        ax.set_xlim3d(DEFAULT_XLIM3D)
        ax.set_ylim3d(DEFAULT_YLIM3D)
        ax.set_zlim3d(DEFAULT_ZLIM3D)

        for vector in self.vectors:
            ax.quiver(
                0, 0, 0,
                vector.x, vector.y, vector.z,
                color="red"
            )

        for point in self.points:
            ax.scatter(point.x, point.y, point.z, color="blue")

        for line in self.lines:
            xy_intersection = Intersection.line_plane(line, XY_PLANE)
            yz_intersection = Intersection.line_plane(line, YZ_PLANE)
            ax.plot(
                [xy_intersection.x, yz_intersection.x],
                [xy_intersection.y, yz_intersection.y],
                [xy_intersection.z, yz_intersection.z],
                color="green"
            )

        if show:
            plt.show()
