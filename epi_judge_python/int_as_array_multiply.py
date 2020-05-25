from test_framework import generic_test
# FAILED


def multiply(num1, num2):
    sign = 1
    if num1[0] < 0 and num2[0] > 0:
        sign = -1
    elif num1[0] > 0 and num2[0] < 0:
        sign = -1

    num1[0] = abs(num1[0])
    num2[0] = abs(num2[0])

    end_array = [0] * (len(num1) + len(num2))

    for i1 in reversed(range(len(num1))):
        for i2 in reversed(range(len(num2))):
            end_array[i1 + i2 + 1] += num1[i1] * num2[i2]
            end_array[i1 + i2] += end_array[i1 + i2 + 1] // 10
            end_array[i1 + i2 + 1] = end_array[i1 + i2 + 1] % 10

    end_array = end_array[next((i for i, x in enumerate(end_array) if x != 0), len(end_array)):] or [0]
    return [sign * end_array[0]] + end_array[1:]


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("int_as_array_multiply.py",
                                       'int_as_array_multiply.tsv', multiply))
