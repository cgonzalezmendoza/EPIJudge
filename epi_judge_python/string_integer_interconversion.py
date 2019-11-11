from test_framework import generic_test
from test_framework.test_failure import TestFailure


def int_to_string(x):
    neg_bool = False
    if x < 0:
        neg_bool = True
        x = x * -1
    number_dict = {0: "0", 1: "1", 2: "2", 3: "3", 4:"4", 5: "5", 6: "6", 7: "7", 8: "8", 9: "9"}
    starting_point = x % 10
    str_arr = [number_dict[starting_point]]
    x = x // 10
    while x > 0:
        str_arr.append(number_dict[x % 10])
        x = x // 10
    if neg_bool:
        str_arr.append("-")
    str_arr.reverse()
    return ''.join(str_arr)


def string_to_int(s):
    neg_bool = False
    if s[0] == "-":
        neg_bool = True
        s = s[1:]
    number_dict = {"0": 0, "1": 1,"2": 2,"3": 3, "4": 4, "5": 5, "6": 6,"7": 7,"8": 8,"9": 9}
    s.split()
    int_arr = [number_dict[x] for x in s]
    rolling_num = 0
    for index, value in enumerate(int_arr):
        rolling_num += (10 ** (len(int_arr) - index - 1)) * value
    if neg_bool:
        rolling_num = rolling_num * -1
    return rolling_num


def wrapper(x, s):
    if int_to_string(x) != s:
        raise TestFailure("Int to string conversion failed, expected:" + s + " got:" + int_to_string(x))
    if string_to_int(s) != x:
        raise TestFailure("String to int conversion failed, expected:" + s + "got:" + str(string_to_int(s)) )


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("string_integer_interconversion.py",
                                       'string_integer_interconversion.tsv',
                                       wrapper))

