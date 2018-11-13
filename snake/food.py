from snake.spatial import Coordinate

import random


class Food:
    def __init__(self, maze_size, snake_map=[]):
        maze_map_free = [Coordinate(x, y) for x in range(maze_size)
                         for y in range(maze_size) if Coordinate(x, y) not in snake_map]
        self._location = random.choice(maze_map_free)
        self._eaten = False

    @property
    def location(self):
        return self._location

    @property
    def eaten(self):
        return self._eaten
