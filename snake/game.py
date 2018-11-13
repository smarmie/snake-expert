from snake.spatial import Coordinate
from snake.snake import Snake
from snake.food import Food

from threading import Timer


_MAZE_SIZE = 10


class PlaySnake:
    def __init__(
            self,
            maze_size=_MAZE_SIZE,
            start_location=Coordinate(int(_MAZE_SIZE/2), int(_MAZE_SIZE/2)),
            tick_interval=1
    ):
        self._maze_size = maze_size
        self._snake = Snake(head=start_location)
        self._food = None
        self._running = False
        self._timer = None
        self._tick_interval = tick_interval
        self._tick_count = 0

    @property
    def score(self):
        return self._snake.length

    @property
    def running(self):
        return self._running

    @property
    def direction(self):
        return self._snake.heading

    @direction.setter
    def direction(self, direction):
        self._snake.heading = direction

    @property
    def game_map(self):
        game_map = [[0 for x in range(self._maze_size)]
                    for y in range(self._maze_size)]
        for segment in self._snake.map:
            game_map[segment.x][segment.y] = 1
        game_map[self._snake.head.x][self._snake.head.y] = 2
        game_map[self._food.location.x][self._food.location.y] = 3
        return game_map

    def start(self):
        if self._running:
            return
        self._timer = Timer(self._tick_interval, self._tick)
        self._food = Food(maze_size=self._maze_size, snake_map=self._snake.map)
        self._timer.start()
        self._running = True

    def stop(self):
        if self._timer:
            self._timer.cancel()
        self._running = False
        self._timer = None

    def _tick(self):
        if not self._running:
            return
        self._timer = Timer(self._tick_interval, self._tick)
        self._timer.start()
        if self._snake.new_head(self._snake.heading) == self._food.location:
            self._snake.move(maze_size=self._maze_size, grow=True)
            self._food = Food(maze_size=self._maze_size, snake_map=self._snake.map)
        else:
            self._snake.move(maze_size=self._maze_size, grow=False)
        if not self._snake.alive:
            self.stop()
