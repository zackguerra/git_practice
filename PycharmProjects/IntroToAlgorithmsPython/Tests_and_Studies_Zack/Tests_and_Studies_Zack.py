# Python Operators

# Adition
from typing import List, Tuple

number_adition = 10

print(number_adition + 5)
print(10 * 3)

# Subtraction
print(1002 - 452)
print(50 - 70)

# Multiplication
number_multi = 2
print(number_multi * 2)
print(number_multi * 10)

# Float Division
print(3 / 2)
print(9 / 2)

# Integer Division
print(3 // 2)
print(9 // 2)

# Exponential
print(2 ** 2)
print(10 ** 2)

# Remainder
print(3 % 2)
print(9 % 2)
print(8 % 2)
print(10 % 5)

# Python Strings
name = "Zack"
mychar = 'Guerra'

print(name, mychar)

name1 = str()  # this will create empty string object
name2 = "newstring"  # string object containing 'newstring'

print(name1)
print(name2)

# About Python's Immutability
str1: str = "welcome"
str2 = "welcome"

id(str1)
id(str2)

str1 += " mike"
id(str1)

print(id(str1), id(str2))

str1 += " mike"

print(str1)

print(id(str1))

# Concatenating
s = "Tom and " + "Jerry"

print(s)

x = "spamming is bad " * 3
print(x)

# Slicing string

z = "Zack Guerra"
c = " Junior"
# Zack Guerra
# 0123456789
print(z[0:3])
print(z[6:11])
print(z[0:])
print(z[4:4])  # Space
print(z[6:11] + c[0:5])  # Testing two slices at once

# String Functions LEN MAX and MIN

text = "Vancouver"

print(len("text"))  # 4 (returns length of the string)

print(max("text"))  # x (value 88) (returns character having highest ASCII value)

print(min("text"))  # e (returns character having lowest ASCII value)

# in and not in operators

txt1 = "Jamaica"

print("lala" in txt1)  # False
print("maic" in txt1)  # True
print("maic" not in txt1)  # False

# Creating list in python

list1: Tuple[int, int, int, int, int] = 1, 2, 3, 4, 5  # Creating a list with integers
list2 = "John", "Jack", "Derrick", "Jose"  # Creating a list with Strings
list3 = "Python"  # Creating a list with characters p,y,t,h,o,n

print(list1)
print(list2)
print(list3)

list4 = list([10, 11, 12, 13, 14, 15])  # Other way to create a list
print(list4)

# Examples of lists using functions

print(len("list1"))
print(max("list1"))
print(max("list1"))
print(sum(list1))

# List slicing
list5 = [10, 11, 12, 13, 14, 15]
print(list5[1:4])

# + and * operators in list

list5 = [10, 11, 12, 13, 14, 15]
list9 = [1, 2, 3, 4, 5]

list6 = list5 * 2
list7 = list6 + list9

print(list6)
print(list7)

# In  or Not In Operator (Using Lists)

print(20 in list6)
print(20 not in list6)
print(11 in list6)
print(11 not in list6)

# VERIFY BELOW !!!

# Commonly used list methods with return type

list10 = [10, 11, 12, 13, 14, 10, 11]
print(list10)
list10.append("15")
print(list10)
# add an element in the end of the list and returns

print(list10.count("10"))


# Creating a Dictionary (Dictionaries can be created using a pair of curly braces ({}) )

friends = {
    "NAME": "111.222.333",
    "Address": "345.678.981",
    "Age": "548.547.632",
    "Goku": "666.999.666",
    "Drake": "234.586.124"
}

# Retrieving, modifying and adding elements in the dictionary

print(friends["Doug"])  # To get an item from the dictionary
print(friends["Jack"])
print(friends["Goku"])
friends["John"] = "111.222.335"  # To add or modify an item
print("Thia are my friends")
print(friends)
