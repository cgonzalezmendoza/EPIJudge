from test_framework import generic_test


def search_first_of_k(A, k):
    L, R = 0, len(A) - 1
    index = -1
    while L <= R:
        mid = L + (R - L) // 2
        if A[mid] == k:
            index = mid
            R = mid - 1
        elif A[mid] < k:
            L = mid + 1
        else:
            R = mid - 1
        print(mid)
    return index


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main(
            "search_first_key.py", 'search_first_key.tsv', search_first_of_k))
