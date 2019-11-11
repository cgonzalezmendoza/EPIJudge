import collections
import copy
import functools

from test_framework import generic_test
from test_framework.test_failure import TestFailure
from test_framework.test_utils import enable_executor_hook

WHITE, BLACK = range(2)

Coordinate = collections.namedtuple('Coordinate', ('x', 'y'))


def search_maze(maze, s, e):
    # Returns a bool, and the path if it exists
    path = []

    def helper(start):
        if start.x >= len(maze) or start.y >= len(maze[0]) or start.x < 0 or start.y < 0:
            return False
        elif maze[start.x][start.y] == BLACK:
            return False
        path.append(start)
        maze[start.x][start.y] = BLACK
        if start == e:
            return True
        else:
            right_found = helper(Coordinate(start.x + 1, start.y))
            if right_found:
                return right_found
            left_found = helper(Coordinate(start.x - 1, start.y))
            if left_found:
                return left_found
            up_found = helper(Coordinate(start.x, start.y + 1))
            if up_found:
                return up_found
            down_found = helper(Coordinate(start.x, start.y - 1))
            if down_found:
                return down_found

            del path[-1]
            return False

    solvable = helper(s)
    if solvable:
        return path
    else:
        return False


def path_element_is_feasible(maze, prev, start):
    if not ((0 <= start.x < len(maze)) and
            (0 <= start.y < len(maze[start.x])) and maze[start.x][start.y] == WHITE):
        return False
    return start == (prev.x + 1, prev.y) or \
           start == (prev.x - 1, prev.y) or \
           start == (prev.x, prev.y + 1) or \
           start == (prev.x, prev.y - 1)


@enable_executor_hook
def search_maze_wrapper(executor, maze, s, e):
    s = Coordinate(*s)
    e = Coordinate(*e)
    cp = copy.deepcopy(maze)

    path = executor.run(functools.partial(search_maze, cp, s, e))

    if not path:
        return s == e

    if path[0] != s or path[-1] != e:
        raise TestFailure("Path doesn't lay between start and end points")

    for i in range(1, len(path)):
        if not path_element_is_feasible(maze, path[i - 1], path[i]):
            raise TestFailure("Path contains invalid segments")

    return True


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("search_maze.py", 'search_maze.tsv',
                                       search_maze_wrapper))
