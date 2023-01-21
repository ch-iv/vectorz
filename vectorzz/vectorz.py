"""This module provides a class for 2D and 3D vectors
 as well as utility functions for them"""
from __future__ import annotations

import math
from typing import Self


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
        coefficient_values = [
            self.direction_vector.x / other.direction_vector.x,
            self.direction_vector.y / other.direction_vector.y,
            self.direction_vector.z / other.direction_vector.z
        ]
        return len(set(coefficient_values)) == 1

    def contains_point(self, point: P3) -> bool:
        """Checks if a specific point is on the line"""
        # A vector is in the form r = origin_vec + t * direction_vec
        # A point is on the line if there exists a t such that
        # r = point

        # calculate t values for each component
        t_values = [
            (point.x - self.origin_vector.x) / self.direction_vector.x,
            (point.y - self.origin_vector.y) / self.direction_vector.y,
            (point.z - self.origin_vector.z) / self.direction_vector.z
        ]
        # the point is on the line if all t values are equal
        return len(set(t_values)) == 1

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

    def is_parallel(self, other: Plane) -> bool:
        """Checks if two planes are parallel"""
        return is_scalar_multiple(self.normal, other.normal)


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
