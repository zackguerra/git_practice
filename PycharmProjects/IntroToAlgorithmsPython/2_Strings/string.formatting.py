# Escape characters
# - newline: "\n"
# - tab: "\t"
# - quotes: \"

city = "va\nc\"ou\tver"
print(city)

dont_worry = "Don't worry about \"the weather!\""
print(dont_worry)
# Slovak
message = "Ahoj, \nako sa mas?\n Ya som OK!"
print(message)

phrase = """
Ahoj,
ako sa mas?
Ya som OK!
"""
print(phrase)

# String formatting
# *formatting chars
# %s: string
# %d: decimal (integer)7
# %f: float

name = "Derrick"
city = "Vancouver"
temp = 8
message1 = "Hello, %s! My name is %s. The temp is %d today" % (city, name, temp)
print(message1)

country = "Canada"
message2 = f"{country} is big!"  # string interpolation
print(message2)

average_point = 80.532154
# 80.5
# variable:{width}.{width_value}
# 80.532154
#
# "          "
# " 80.5"

print(f'The average point is {average_point:{5}.{3}}')  # 5 is the number of chars, 3 is the number to display
print("The average point is %.1f" % average_point)

x = 10
y = 17
# print(f"{x} x {y} = {x * y}"
