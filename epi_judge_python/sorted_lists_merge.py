from test_framework import generic_test


def merge_two_sorted_lists(L1, L2):
    if not L1 and not L2:
        return None
    if not L1:
        return L2
    if not L2:
        return L1

    if L1.data < L2.data:
        starting_point = L1
        L1 = L1.next
    else:
        starting_point = L2
        L2 = L2.next
    sentinel = starting_point

    while L1 and L2:
        if L1.data < L2.data:
            starting_point.next = L1
            starting_point = starting_point.next
            L1 = L1.next
        else:
            starting_point.next = L2
            starting_point = starting_point.next
            L2 = L2.next

    if L1:
        starting_point.next = L1
    elif L2:
        starting_point.next = L2

    return sentinel




    return sentinel


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("sorted_lists_merge.py",
                                       'sorted_lists_merge.tsv',
                                       merge_two_sorted_lists))
