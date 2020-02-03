# Methods --> Functions that belong to String type
# str.method()  (dot operator to call methods)
# method() --> `()` call, execute, run


city = "vancouver"

# 1. Capitalize
print(city.capitalize())  # Vancouver

# 2. Uppercase(A), Lowercase(a)
upper_city = city.upper()
print(upper_city)
lower_city = city.lower()
print(lower_city)

# 3.
#    index: returns th index of substring (no match will cause error)
#    find: returns the index of substring (no match will return -1)
# vancouver
# 012345678
print(city.index("o")) # 4
print(city.index("cou")) # 3
# print(city.index("x"))  # Error
print(city.find("ver")) # 6
print(city.find("x")) # -1 (does not exists)

# 4. count: returns the occurrences of substring in string
#    * case-sensitive (0)  vs  case-insensitive

food = "poutine donut tacos\nbig-mac pizza"
print(food)
print(food.count("o"))
print(food.count(" "))  # space is a character (ASCII 32)

# 5. `in`  : to check whether some string is in another string
greeting = "hello world"
message = "hello"
print(message in greeting)  # true

# 6. String validation
#    isalnum(): checks if string has alphanumeric chars (alphabets + numbers)
#    isalpha(): checks if string has alphabets chars (only alphabets)
#    isdigits(): checks if string has digits (only numbers)
#    isupper():
#    islower():
#    isspace(): check if string has whitespace chars
#               - space(" "), tab("\t"), newline("\n")

unit_num = "123"
street_name = "Robson"

print(unit_num.isdigit())  # true
print(street_name.isalpha())  # true

