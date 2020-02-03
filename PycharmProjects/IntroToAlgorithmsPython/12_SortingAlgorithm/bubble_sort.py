# Bubble Sort
# - Time Complexity: O(n^2)
#
# For each scan,
#    For each comparison (two adjacent items),
#        if left item > right item:
#            "swap" two items


items = [5, 2, 1, 4, 3]


# Naive Bubble Sort -> can be improved!
def naive_bubble_sort(items):
    steps = 0
    for scan in range(len(items)):
        for j in range(len(items) - 1):
            steps += 1
            if items[j] > items[j+1]:
                items[j], items[j+1] = items[j+1], items[j]
    print(steps)


def bubble_sort(items):
    steps = 0
    for scan in range(len(items)):
        is_swapped = False
        for j in range(len(items) - 1 - scan):
            steps += 1
            if items[j] > items[j+1]:
                # swap
                items[j], items[j+1] = items[j+1], items[j]
                is_swapped = True
        if not is_swapped:
            break
    print(steps)