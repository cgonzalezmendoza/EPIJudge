from test_framework import generic_test
import heapq


def merge_sorted_arrays(sorted_arrays):
    min_heap = []
    return_arr = []
    for index, arr in enumerate(sorted_arrays):
        min_heap.append((arr[0], (index, 0)))
    heapq.heapify(min_heap)
    while min_heap:
        val, cords = heapq.heappop(min_heap)
        row, col = cords
        return_arr.append(val)
        col+= 1
        if len(sorted_arrays[row]) > col:
            heapq.heappush(min_heap, (sorted_arrays[row][col],(row,col)))

    return return_arr


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("sorted_arrays_merge.py",
                                       "sorted_arrays_merge.tsv",
                                       merge_sorted_arrays))
