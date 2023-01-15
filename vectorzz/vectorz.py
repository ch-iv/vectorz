"""This module provides a class for 2D and 3D vectors
 as well as utility functions for them"""

import math
from typing import Self


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
        return f"({self.x}, {self.y}, {self.z})"

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


class Vec2:
    """Represents a 2D vector with x and y components."""
    def __init__(self, x, y):
        # the x component of the vector
        self.x = x
        # the y component of the vector
        self.y = y

    def __str__(self):
        return f"({self.x}, {self.y})"

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
