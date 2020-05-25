from test_framework import generic_test


def smallest_nonconstructible_value(A):
    A.sort()
    run_sum = 0
    for val in A:
        if val > run_sum and val != run_sum + 1:
            return run_sum + 1
        else:
            run_sum += val

    return run_sum + 1


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("smallest_nonconstructible_value.py",
                                       'smallest_nonconstructible_value.tsv',
                                       smallest_nonconstructible_value))
