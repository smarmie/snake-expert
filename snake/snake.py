from snake.spatial import (
    Coordinate,
    Directions,
)


class Snake:
    def __init__(self, head=Coordinate(0, 0), direction=Directions.DOWN):
        self._alive = True
        self._head = head
        self._heading = direction
        self._body = []

    @property
    def alive(self):
        return self._alive

    @property
    def length(self):
        return len(self._body) + 1

    @property
    def heading(self):
        return self._heading

    @heading.setter
    def heading(self, heading):
        if self.length > 0 and \
                    self._head + heading == self._body[0]:
            # do nothing, we're trying to move backwards
            pass
        else:
            self._heading = heading

    @property
    def head(self):
        return self._head

    @property
    def map(self):
        return [self._head] + self._body

    def new_head(self, move):
        return self._head + move

    def move(self, maze_size, grow=False):
        new_head = self._head + self._heading
        if new_head in self._body[:-1] or \
                new_head.x == maze_size or \
                new_head.y == maze_size or \
                new_head.x == -1 or \
                new_head.y == -1:
            self._alive = False
        else:
            self._body.insert(0, self._head)
            self._head = new_head
            if not grow:
                self._body.pop()
