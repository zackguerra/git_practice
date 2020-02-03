# String (str) : A sequence of characters in "" or ''

# + Concatenation: combining two strings
print("hello " + "world")

# * multiplication: repeat strings
print("hello" * 5)  # Hello 5 times

# String indexing (index == position)
singer = "Lady Gaga"
# index 012345678
# index "always" starts from "0"

print(singer[0])  # "L"
print(singer[7])  # "g"
print(singer[-1])  # "a"

# print(singer[-15])  # Error (index out of bounds)


# String Slicing (Substring)
# start_index <=   < end_index

actor = "Will Smith"
# index  0123456789
print(actor[0:4])  # "Will"
print(actor[2:6])  # "ll S"
print(actor[-3:-1])  # "it"

# shortcuts
# starting at 0
print(actor[:4])

# go to the end
print(actor[5:])

# from 0 to the end (copy)
print(actor [:])

# How to get the number of characters?
# len(): returns the number of chars

print(len(actor))  # 10 (incorrect)
print(actor[len(actor) - 1])  # 10 - 1 = 9 'last char'
print(actor [-1])  # 'last char'

# Strings are "IMMUTABLE" (you cant change)
# I can't change the internals (characters)
ball_player = "Lebron James"
# ball_player[0] = "T" (error, DO NOT TRY TO MUTATE STRING)



