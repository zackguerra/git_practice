# Selection Sort
# Time Complexity: O(n^2)
#
# For each scan from 0 to len(items) - 1
#     find the index of the minimum item (linear search)
#     swap the minimum item with items[scan]
#

import bubble_sort

def naive_selection_sort(items):
    steps = 0
    for scan in range(len(items)):
        min_index = scan
        for i in range(scan, len(items)):
            steps += 1
            if items[i] < items[min_index]:
                min_index = i
        # swap
        items[scan], items[min_index] = items[min_index], items[scan]

    print(steps)


def selection_sort(items):
    steps = 0
    for scan in range(len(items) - 1):
        min_index = scan
        for i in range(scan + 1, len(items)):
            steps += 1
            if items[i] < items[min_index]:
                min_index = i

        if min_index != scan:  # we did not find a smaller item
            # swap
            items[scan], items[min_index] = items[min_index], items[scan]

    print(steps)