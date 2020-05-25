from test_framework import generic_test


def convert_base(num_as_string, b1, b2):
    if num_as_string == "0" or num_as_string == "-0":
        return num_as_string
    negative = num_as_string[0] == "-"
    if negative:
        num_as_string = num_as_string[1:]
    conversion_dict = {10: 'A', 11: 'B', 12: 'C', 13: 'D', 14: 'E', 15: 'F'}
    for i in range(10):
        conversion_dict[i] = str(i)
    decimal = int(num_as_string, base=b1)
    return_arr = []
    quotient = decimal

    while quotient != 0:
        remainder = quotient % b2
        quotient = quotient // b2
        return_arr.append(conversion_dict[remainder])
    if negative:
        return_arr.append("-")
    return "". join(reversed(return_arr))


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("convert_base.py", "convert_base.tsv",
                                       convert_base))
