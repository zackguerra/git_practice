#  Operators
#  +, -, *, /, // (floor division)
#  % (modulo): 'mod' remainder
#  ** (power)
print(10 % 3)  # 1
print(10 ** 2)  # 100
print(100 // 3)  # 33

#  = : assignment

number = 7
number = number + 3  # increment number by 3

#  += : increment number

number += 3  # increment number by 3

#  -= : decrement number

number -= 3  # decrement number by 3
print("number = " + str(number))  # string concatenation(combine) (+)

#  *= : multiply by
number *= 2  # number = number * 2

#  /= : divided by
number /= 2  # number = number / 2

# Boolean Operators
# Comparison
# == : equality (equal)
# != : not equal to

print (3 == 4)  # False

# > : greater than
# < : less than
# >= : greather than or equal to
# <= : less than or equal to

print(3 < 4)  # True

#  check if x is greater than equal to 7 and less than 12
x = 10

#  A 'and' B: both A and B have to be True to return True
#  A 'or' B: either A or B has to be True to return True

print(x >= 7 and x < 12)  # and, or

# print (x >= 7 and x < 12)
print(7 <= x < 12)  # python way (only)
print((3 != 3) or (4 == 4))

#Exercice
num = 10

print(num > 1) and (num / 0 == 0)  # ZeroDivisionError
print((num > 10) and (num / 0 == 0 ))  # False
print(num > 1) or (num / 0 == 0))  # True
print(num >10) or (num / 0 == 0))  # ZeroDivisionError
print(not True)  # False
print(not False)  # True


address = 255.100.1.1
