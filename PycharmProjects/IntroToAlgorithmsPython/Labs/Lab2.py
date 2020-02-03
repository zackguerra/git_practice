"""
Basic python list problems -- no loops.
"""


def first_last6(nums):
    """
    Given a list of ints, return True if 6 appears as either the first or last element in the list.
    The list will be length 1 or more.
    """
    pass

    if 6 == nums[0] or 6 == nums[-1]:
        return True
    else:
        return False


def same_first_last(nums):
    """
    Given a list of ints, return True if the list is length 1 or more, and the first element
    and the last element are equal.
    """
    pass

    # Java --> 2+2=4?True:False
    if len(nums) >= 1 and nums[0] == nums[-1]:
        return True
    else:
        return False



def common_end(a, b):
    """
    Given 2 lists of ints, a and b, return True if they have the same first element or they have the same last element.
    Both lists will be length 1 or more.
    """
    pass


    if a[0] == b[0] or a[-1] == b[-1]:
        return(True)
    else:
        return(False)



def sum3(nums):
    """
    Given a list of ints length 3, return the sum of all the elements.
    """
    pass

    return(sum(nums))


def rotate_left3(nums):
    """
    Given a list of ints length 3, return a list with the elements "rotated left" so {1, 2, 3} yields {2, 3, 1}.
    """
    pass

    nums.append(nums[0])
    return(nums[1:])


def reverse3(nums):
    """
    Given a list of ints length 3, return a new list with the elements in reverse order,
    so {1, 2, 3} becomes {3, 2, 1}.
    """
    pass

    nums.reverse()
    return(nums)
    # return nums[::-1] --> same function


def max_ends3(nums):
    """
    Given a list of ints length 3, figure out which is larger, the first or last element in the list,
    and set all the other elements to be that value. Return the changed list.
    """
    pass

    if nums[0] > nums[-1]:
        big = nums[0]
    else:
        big = nums[-1]
    listbig = []
    listbig.append(big)
    listbig.append(big)
    listbig.append(big)
    return(listbig)


def make_ends(nums):
    """
    Given a list of ints, return a new list length 2 containing the first and last elements from the original list.
    The original list will be length 1 or more.
    """
    pass

    if len(nums) < 1:
        return False
    else:
        list = [nums[0], nums[-1]]
        return list


def has23(nums):
    """
    Given an int list length 2, return True if it contains a 2 or a 3.
    """
    pass

    if 2 in nums or 3 in nums:
        return True
    else:
        return False