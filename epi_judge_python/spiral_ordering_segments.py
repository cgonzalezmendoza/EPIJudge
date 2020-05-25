from test_framework import generic_test
import collections
# FAILURE


def matrix_in_spiral_order(square_matrix):
    if not square_matrix:
        return []
    path = []
    visited = set()
    c = r = 0
    directions = [(1, 0), (0, 1), (-1, 0), (0, -1)]
    current_dir = 0
    for _ in range(len(square_matrix) ** 2):
        path.append(square_matrix[c][r])
        visited.add((c, r))
        next_c = c + directions[current_dir][1]
        next_r = r + directions[current_dir][0]
        if next_c not in range(len(square_matrix)) or next_r not in range(len(square_matrix[0])) or (next_c, next_r) in visited:
            current_dir = (current_dir + 1) % 4
            next_c = c + directions[current_dir][1]
            next_r = r + directions[current_dir][0]
        c = next_c
        r = next_r

    return path


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("spiral_ordering_segments.py",
                                       "spiral_ordering_segments.tsv",
                                       matrix_in_spiral_order))
