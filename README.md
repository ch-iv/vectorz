[![CodeFactor](https://www.codefactor.io/repository/github/ch-iv/vectorz/badge)](https://www.codefactor.io/repository/github/ch-iv/vectorz)
# Vectorz
Vectorz is a library for working with 2D and 3D vectors in Java. It is designed to be fast, flexible, and easy to use.
It provides functionality for creating vectors and performing operations on them, such as addition, subtraction, dot product, cross product, and more.

## Examples

Creating a 3D Vector
```python
from vectorz import Vec3

# Create a vector
v = Vec3(1, 2, 3)
# Calculate the magnitude (length) of the vector
v.magnitude()
```

Operations on vectors
```python
v1 = Vec3(1, 2, 3)
v2 = Vec3(4, 5, 6)
# Add two vectors
result = v1 + v2  # (5, 7, 9)
# Subtract two vectors
result = v1 - v2  # (-3, -3, -3)
# Multiply by a scalar value
result = -1.25 * v1 # (-1.25, -2.5, -3.75)
# Divide by a scalar value
result = v1 / 2 # (0.5, 1.0, 1.5)
```

Advanced vector operations
```python
from vectorz import Vec3, dot, cross

v1 = Vec3(1, 2, 3)
v2 = Vec3(4, 5, 6)
# Calculate the dot product of two vectors
dot(v1, v2)  # 32
# Calculate the cross product of two vectors
cross(v1, v2)  # (-3, 6, -3)
```
