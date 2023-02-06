import math


class MyMath:
    """Математический класс"""

    @classmethod
    def circle_len(cls, radius: int) -> int:
        """Функция, возвращающая длину окружности"""

        return 2 * math.pi * radius

    @classmethod
    def circle_sq(cls, radius: int) -> int:
        """Функция, возвращающая площадь окружности"""

        return math.pi * radius ** 2

    @classmethod
    def cube_vol(cls, side_len: int) -> int:
        """Функция, возвращающая объем куба"""

        return side_len ** 3

    @classmethod
    def sphere_sq(cls, radius: int) -> int:
        """Функция, возвращающая площадь поверхности сферы"""

        return 4 * math.pi * radius ** 2