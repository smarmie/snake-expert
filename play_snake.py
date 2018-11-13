import curses
import threading
from snake.spatial import Directions
from snake.game import PlaySnake

_TICK = 1000
_MAZE_SIZE = 20


def draw_screen(stdscr, game):
    while game.running:
        game_map = game.game_map
        line = 0
        for i in game_map:
            stdscr.addstr(line, 0, ''.join([str(x) for x in i]))
            line += 1
        # Refresh the screen
        stdscr.refresh()


def play_snake(stdscr):
    stdscr.clear()
    stdscr.refresh()
    curses.curs_set(0)
    game = PlaySnake(maze_size=_MAZE_SIZE)
    game.start()
    thread = threading.Thread(target=draw_screen,
                              kwargs={
                                  'stdscr': stdscr,
                                  'game': game,
                              })
    thread.start()
    k = 0
    while k != ord('q') and game.running:
        if k == curses.KEY_DOWN:
            game.direction = Directions.DOWN
        elif k == curses.KEY_UP:
            game.direction = Directions.UP
        elif k == curses.KEY_RIGHT:
            game.direction = Directions.RIGHT
        elif k == curses.KEY_LEFT:
            game.direction = Directions.LEFT

        # Wait for next input
        k = stdscr.getch()
    if game.running:
        game.stop()

    return game.score


def main():
    score = curses.wrapper(play_snake)
    print("Died with length {}".format(score))


if __name__ == "__main__":
    main()
