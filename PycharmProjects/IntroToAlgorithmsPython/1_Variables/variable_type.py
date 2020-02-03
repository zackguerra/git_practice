#  Data types
#  There are many different data types in Python
#  int: integer
#  float: floating point (10.23, 3.14, etc)
#  bool: boolean (True, False)
#  str: a sequence of characters in quotes"aa", 'a'

language = "en_us"
print(type(language))  # check the type of the variable

users = 10
print(str(users) + language)  # "10" + "en_us" --> "10en_us"

#  Type Conversion (type casting): "changing types"
#  There are several built-in functions that let you convert
#  one data type to another.

#  str(x): converts x into a string representation
#  int(x): converts x into a integer.
#  float(x): converts x into a floating-point number.


#  Exercice: what is the type of following operation?


#  1. 10 / 2 -> float  '/': float division
print(type(10 / 2))

#  2. 10 // 2 -> int      '//': int division
print(type(10 // 4))

#  3. float("a.12") -> Error
#  float(5) -> 5.0 (float)
print(float("a.12"))




