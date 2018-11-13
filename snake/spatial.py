class Coordinate(object):
    def __init__(self, x, y):
        self._x = x
        self._y = y

    @property
    def x(self):
        return self._x

    @property
    def y(self):
        return self._y

    def __add__(self, other):
        return Coordinate(self.x + other.x, self.y + other.y)

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y

    def __str__(self):
        return str((self.x, self.y))

    def __repr__(self):
        return repr((self.x, self.y))


class Directions:
    UP = Coordinate(-1, 0)
    DOWN = Coordinate(1, 0)
    LEFT = Coordinate(0, -1)
    RIGHT = Coordinate(0, 1)
