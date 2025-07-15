import cmath
from typing import Union


class Vector2D:
    def __init__(self, x, y):
        self.__val = complex(x, y)

    def __eq__(self, other: "Vector2D"):
        return self.__val == other.__val

    def __mul__(self, other: Union[float, complex, "Vector2D"]) -> "Vector2D":
        if type(other) is type(self):
            other = other.__val
        return Vector2D.from_complex(self.__val * other)

    def __add__(self, other: Union[float, complex, "Vector2D"]) -> "Vector2D":
        if type(other) is type(self):
            other = other.__val
        return Vector2D.from_complex(self.__val + other)

    def __sub__(self, other: Union[float, complex, "Vector2D"]) -> "Vector2D":
        if type(other) is type(self):
            other = other.__val
        return Vector2D.from_complex(self.__val - other)

    def __mod__(self, other: "Vector2D") -> "Vector2D":
        return Vector2D(
            self.__val.real % other.__val.real, self.__val.imag % other.__val.imag
        )

    def __truediv__(self, other: Union[float, complex, "Vector2D"]) -> "Vector2D":
        if type(other) is type(self):
            other = other.__val
        return Vector2D.from_complex(self.__val / other)

    def __iter__(self):
        return iter([self.__val.real, self.__val.imag])

    def __str__(self):
        return str(f"[x: {self.__val.real}, y: {self.__val.imag}]")

    @staticmethod
    def from_complex(complex_num: complex):
        return Vector2D(complex_num.real, complex_num.imag)

    @property
    def angle(self, degrees=True) -> float:
        angle = cmath.phase(self.__val)
        if degrees:
            angle = angle / cmath.pi * 180
        return angle

    @property
    def length(self) -> float:
        return self.dot(self) ** 0.5

    def limit(self, limit: float) -> "Vector2D":
        length = self.length
        if length > limit:
            ratio = limit / length
            return self * ratio
        return self

    def set_length(self, length: float) -> "Vector2D":
        if self == Vector2D(0, 0):
            return Vector2D(length, 0)
        ratio = length / self.length
        return self * ratio

    def dot(self, other: "Vector2D") -> float:
        return self.__val.real * other.__val.real + self.__val.imag * other.__val.imag

    def project_on(self, other: "Vector2D") -> "Vector2D":
        return other * self.dot(other) / other.dot(other)

    def rotate(self, angle: float):
        pass
