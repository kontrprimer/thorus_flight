class Vector:
    def __init__(self, coordinates):
        self.__coordinates = list(coordinates)

    def __len__(self):
        return len(self.__coordinates)

    def __eq__(self, other: "Vector"):
        return self.__coordinates == other.__coordinates

    def __mul__(self, num: float):
        return Vector([x * num for x in self.__coordinates])

    def __add__(self, other: "Vector") -> "Vector":
        return Vector([i + j for i, j in zip(self.__coordinates, other.__coordinates)])

    def __sub__(self, other: "Vector") -> "Vector":
        return Vector([i - j for i, j in zip(self.__coordinates, other.__coordinates)])

    def __mod__(self, other: "Vector") -> "Vector":
        return Vector([i % j for i, j in zip(self.__coordinates, other.__coordinates)])

    def __truediv__(self, other: float) -> "Vector":
        return Vector([i / other for i in self.__coordinates])

    def __iter__(self):
        return iter(self.__coordinates)

    @property
    def length(self) -> int:
        return sum(i**2 for i in self.__coordinates) ** 0.5

    def limit(self, limit: float) -> "Vector":
        length = self.length
        if length > limit:
            ratio = limit / length
            return self * ratio
        return self
