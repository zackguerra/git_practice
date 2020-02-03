""" Sorting Practice Problems """

# Write a program that sorts the first half of a list in ascending order
# and the second half in descending order.

# e.g. alist = [8, 1, 7, 5, 2, 4, 2, 9, 3, 6] the alist should be
# changed to [1, 2, 5, 7, 8, 9, 6, 4, 3, 2]. This should work for other lists of course.


def sort_half(alist):

    def bubble_sort(items):
        for scan in range(len(items)):
            is_swapped = False
            for j in range(len(items) - 1 - scan):
                if items[j] > items[j + 1]:
                    items[j], items[j + 1] = items[j + 1], items[j]
                    is_swapped = True
            if not is_swapped:
                break

    list1 = alist[:len(alist) // 2]
    list2 = alist[len(alist) // 2:]
    bubble_sort(list1)
    bubble_sort(list2)
    list2.reverse()
    list1.extend(list2)

    return list1


# Suppose two lists A and B have already been sorted.
# Elements of A have been sorted into ascending order and
# B has also been sorted in ascending order. Write a Python
# program to merge the elements of A and B into a list.
# At the end of the program the result list will contain
# all the elements of A and B in ascending order.


def merge_two(A, B):
    mainlist = (A + B)

    def bubble_sort(items):
        for scan in range(len(items)):
            is_swapped = False
            for j in range(len(items) - 1 - scan):
                if items[j] > items[j + 1]:
                    items[j], items[j + 1] = items[j + 1], items[j]
                    is_swapped = True
            if not is_swapped:
                break

    bubble_sort(mainlist)

    return(mainlist)


# Write a program to replace all negative values in a list
# called mylist with zeros. So, if mylist = [2, 5, -1, 3, 7, -2, 8],
# then mylist should be changed to [2, 5, 0, 3, 7, 0, 8]. This
# should of course work for other lists.


def replace_negative(mylist):

    list2 = [0 if i < 0 else i for i in mylist]

    return(list2)






