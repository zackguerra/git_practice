"""
Basic python string problems -- no loops.
"""


def hello_name(name):
    """
    Given a string name, e.g. "Bob", return a greeting of the form "Hello Bob!".
    """
    return "Hello " + name + "!"


def make_tags(tag, word):
    """
    The web is built with HTML strings like "<i>Yay</i>" which draws Yay as italic text.
    In this example, the "i" tag makes <i> and </i> which surround the word "Yay".
    Given tag and word strings, create the HTML string with tags around the word, e.g. "<i>Yay</i>".
    """
    return "<" + tag + ">" + word + "</" + tag + ">"


def first_two(string):
    """
    Given a string, return the string made of its first two chars, so the String "Hello" yields "He".
    If the string is shorter than length 2, return whatever there is, so "X" yields "X", and the empty string ""
    yields the empty string "".
    """
    pass

    if len(string) <= 2:
        return string[:2]
    elif len(string) > 2:
        return string[:2]


def first_half(string):
    """
    Given a string of even length, return the first half. So the string "WooHoo" yields "Woo".
    """
    pass

    len(string)
    return string[: len(string) // 2]


def without_end(string):
    """
    Given a string, return a version without the first and last char, so "Hello" yields "ell".
    The string length will be at least 2.
    """
    pass

    len(string)
    return string[1: len(string) - 1]


def non_start(a, b):
    """
    Given 2 strings, return their concatenation, except omit the first char of each.
    The strings will be at least length 1.
    """
    pass

    len(a)
    return a[1: len(a)] + b[1: len(b)]


def left2(string):
    """
    Given a string, return a "rotated left 2" version where the first 2 chars are moved to the end.
    The string length will be at least 2.
    """
    pass

    len(string)
    return string[2: len(string)] + string[0:2]