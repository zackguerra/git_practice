"""
 String, List - Level 2.0
"""


def count_hi(string):
    """
    Return the number of times that the string "hi" appears anywhere in the given string.
    """
    pass

    return string.count("hi")


def cat_dog(string):
    """
    Return True if the string "cat" and "dog" appear the same number of times in the given string.
    """
    pass

    search1 = "cat"
    search2 = "dog"

    if (string.count(search1)) == (string.count(search2)):
        return True
    else:
        return False


def count_code(string):
    """
    Return the number of times that the string "code" appears anywhere in the given string,
    except it'll accept any letter for the 'd', so 'cope' and 'cooe' count.
    """
    pass

    code = 0
    for i in range(len(string)):

        if i + 3 > len(string) - 1:
            break
        if "c" == string[i] and "o" == string[i + 1] and "e" == string[i + 3]:
            code += 1

    return(code)


def end_other(a, b):
    """
    Given two strings, return True if either of the strings appears at the very end of the other string,
    ignoring upper/lower case differences (in other words, the computation should not be "case sensitive").
    Note: s.lower() returns the lowercase version of a string.
    """
    pass

    a = (a.lower())
    b = (b.lower())

    if a.endswith(b) or b.endswith(a):
        return True
    else:
        return False

def count_evens(nums):
    """
    Return the number of even ints in the given list.
    Note: the % 'mod' operator computes the remainder, e.g. 5 % 2 is 1.
    """
    pass

    evens = 0
    for n in range(len(nums)):
        if nums[n] % 2 == 0:
            evens += 1
    return evens


def big_diff(nums):
    """
    Given a list length 1 or more of ints, return the difference between the largest and smallest values in the array.
    Note: the built-in min(v1, v2) and max(v1, v2) functions return the smaller or larger of two values.
    """
    pass

    return max(nums) - min(nums)


def sum13(nums):
    """
    Return the sum of the numbers in the list, returning 0 for an empty array.
    Except the number 13 is very unlucky, so it does not count and numbers that come immediately after a 13 also do not count.
    """
    pass

    sum = 0
    false = False

    for i in range(len(nums)):
        if not false and nums[i] != 13:
            sum = sum + nums[i]
        elif nums[i] == 13:
            false = True
        elif false and nums[i] != 13:
            false = False

    return sum

    # <--->
    total = 0
    i = 0

    while i < len(nums):
        if nums[i] == 13:
            i += 2
        else:
            total += nums[i]
            i += 1
    return total


def sum67(nums):
    """
    Return the sum of the numbers in the list, except ignore sections of numbers starting with a 6
    and extending to the next 7 (every 6 will be followed by at least one 7). Return 0 for no numbers.
    """
    pass

    sum = 0
    j = 0

    for i in range(len(nums)):
        if j == 0:
            if nums[i] == 6:
                j = 1
        elif j == 1 and i > 0 and nums[i - 1] == 7:
            j = 0
        if j == 0:
            sum += nums[i]
    return sum


def has22(nums):
    """
    Given a list of ints, return True if the array contains a 2 next to a 2 somewhere.
    """
    pass



    for i in range(len(nums) - 1):
        if nums[i] == 2 and nums[i + 1] == 2:
            return True

    return False
