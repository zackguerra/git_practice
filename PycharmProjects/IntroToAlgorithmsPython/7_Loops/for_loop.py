# Loops - to repeat code

# for loops are used to iterate over a given sequence.
# on each iteration, the loop variable defined in the for loop will be assigned to be next value(sequence).

# Syntax:
# for __ in collection:
#     what to repeat

# Numbers (simple loop wish a list)
for i in [1, 2, 3, 4, 5]:
    print(i)

# range([start,] end, steps): returns a range of numbers ( "[]"means optional
# - range(end): 0 <= < end, 1 step
# - range(start, end): stard <= < end, 1 step
# - range(start, end, steps): start <= < end, steps

#example
# range(1 , 10) - 1, 2, 3, 4, 5, 6, 7, 8, 9
# range(5) - 0, 1, 2, 3, 4
# range(2, 8, 2) - 2, 4, 6
# range(10, 5, -1) - [10, 9, 8, 7, 6]

for i in range(5):
    print(i)

print("=========================")
for i in range(10, 5, -1):
    print(i)
for i in range(1, 10):
    print(i)


print("=========================")

# Exercise
# 1. Write a loop to print all even numbers from 0 to 100 (inclusive)

for i in range(0, 101, 2):
    print(i)

print("=========================")

# 2. Write a loop to print all odd numbers from 0 to 100 (inclusive)

for i in range(101):
    if i % 2 == 1:
       print(i)


# Strings: a sequence of characters
for ch in "Hello":
    print(ch)

# Lists: a sequence of items
for item in ["hello", "hola", "ahoj", "ahayo", "oi"]:
    print(item)

# (optional) list comprehension
# { x | 0 <= x < 10 }
a = [i for i in range(10) if i % 2 == 0]
print(a)

print("<==Exercice==>")
# print the names that have less than 5 characters from the given list.

names = ["Derrick", "Leo", "Sean", "Richard", "Douglas"]
for name in names:
    if len(name) < 5:
        print(name)


# How to write a for-loop to calculate the following
# 2^0 + 2^1 + ...... + 2^30 ( ex: 2^1 ==> 2 ** 1)

result = 0
for i in range(31):
    result += 2 ** i
    print(result)
    #result = result + 2 ** i

print(result)
print((2 ** 31) - 1)

