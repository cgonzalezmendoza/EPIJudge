from test_framework import generic_test


def power(x, y):
    factor_list = []
    if y == 0:
        return 1
    if y == 1:
        return x
    neg = False
    if y < 0:
        neg = True
        y *= -1
    while y != 1:
        if y % 2 != 0:
            factor_list.append(x)
        x *= x
        y = y // 2
    for factor in factor_list:
        x *= factor
    if neg:
        return 1/x
    return x


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("power_x_y.py", 'power_x_y.tsv', power))
