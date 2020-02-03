# Inexing a list

countries = ["Brazil", "Japan", "Colombia",
             "Slovakia", "Mexico", "Canada",
             "USA", "Korea"]

print(countries[-1])
print(countries[0])
print(len(countries))

# Modify(change, mutate) elements (Lists are MUTABLE)
countries[-1] = "South Korea"
print(countries)

# Slicing lists (end index is not inclusive)
print(countries[0:3])  # 0 <= < 3
countries[5:8] = []  # remove last 3 elements
print(countries)
countries[0:3] = ["U.N."]  # replace 3 first items to "U.N."
print(countries)
print(countries[:3])  # first <=  < 3
print(countries[3:])  # 3 <=  <= end
print(["2", "3"] * 5)  # ["2", "3", "2", "3", "2", "3", .......] 5times

# String vs List
# list can contain different types
# string only contains chars
# strings are immutable
# lists are mutable

li = ["String", 10, True, 3.14, [1, 2, 3]]
l = li[-1][0]  # access a list of lists
print(l)  # 1