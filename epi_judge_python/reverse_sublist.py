from test_framework import generic_test


def reverse_sublist(L, start, finish):
    if finish - start == 0:
        return L

    link_map = dict()
    pointer = L
    vals = [start - 1, start, finish, finish + 1]
    for i in range(1, finish + 2):
        if pointer is None:
            break
        if i in vals:
            link_map[i] = pointer
        pointer = pointer.next

    pointer = link_map[start]
    next_p = pointer.next
    nn_p = next_p.next
    for _ in range((finish - start)):
        next_p.next = pointer
        pointer = next_p
        next_p = nn_p
        if next_p is not None:
            nn_p = next_p.next
        else:
            nn_p = None

    if start - 1 in link_map.keys():
        link_map[start - 1].next = link_map[finish]
    if finish + 1 in link_map.keys():
        link_map[start].next = link_map[finish + 1]
    else:
        link_map[start].next = None

    if start == 1:
        return link_map[finish]
    else:
        return L


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("reverse_sublist.py",
                                       "reverse_sublist.tsv", reverse_sublist))
