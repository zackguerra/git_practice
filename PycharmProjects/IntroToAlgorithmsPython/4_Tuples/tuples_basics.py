# Tuples are almost identical to lists.
# The only big difference between list and tuples is that tuples cannot be modified. (Immutable)
# You cannot add(append). change(replace), or delete elements from the tuple.

# Tuples = "Immutable Lists"

vowels = ("a", "e", "i", "o", "u", "e")  # vowels (a, e, i) consonants (b, c, d, f)
print(vowels[0])
print("k" in vowels)
# vowels[0] = "A" # Error (Immutable)

# Methods
print(vowels.index("e"))
print(vowels.count("e"))

# Use cases
# 1. return multiple values from a function


def a():
    return 1, "Mars"  # Tuple (optional parenthesis)

# 2. check if fan item is in a tuple
print("a" in vowels)

# 3. multiple assignments
year, country = (2020, "Canada")

# swap
x = 10
y = 20
x, y = y, x
print(x, y)

# other languages
temp = x
x = y
y = temp

# x = 20, y = 10
