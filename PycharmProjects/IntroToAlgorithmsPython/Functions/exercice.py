def mrange(start, end, steps=1):  # default param
    """"
    Returns a list of integers from start to end by steps
    ex) start <= i < end, skipped by steps
    :param start:
    :param end:
    :param steps:
    :return: a list of numbers within the range
    """
    alist = []
    # TODO your logic goes here (try NOT to use range())
    # While-loop

    alist = []
    while start < end:
        alist.append(start)
        start += steps
    return alist


print(mrange(1, 10))
print(mrange(1, 10, 2))

# *args
# takes arbitrary number of arguments as Tuple
def xrange(*args):
    if len(args) == 1:
        return mrange(0, args[0])
    elif len(args) == 2:
        return mrange(args[0], args [1])
    elif len(args) == 3:
        return mrange(*args)
    else:
        # raise an Error by yourself
        raise TypeError("Invalid Number of Arguments!")

print(xrange(1, 10, 2))
# print(xrange(1, 10, 2, 5, 6))  # Error
