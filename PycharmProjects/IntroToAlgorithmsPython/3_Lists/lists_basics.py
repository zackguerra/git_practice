# Data Structure
# list: A sequence of items (elements)

# 1. create a list
squares = [1, 4, 9, 16, 25, 36, 49]
print(squares)

# 2. list operations
squares += [64, 84]  # add two elements at the end of the list
print(squares)

# 4. list methods

animals = ["Panda", "Eagle", "Beaver", "Kangaroo", "Rooster", "Jaguar", "Monkey", "Panda", "Condor"]

animals.append("Dog")  # add "Dog" to the end of the list
print(animals)
animals.insert(0, "Cat")  # insert "Cat" ad 0 index
print(animals)
animals.remove("Rooster")  # remove "Rooster" from the list, returns None
print(animals)
print(animals.pop(0))  # pop(remove) the element at index 0 and returns the popped element
print(animals)
print(animals.count("Beaver"))  # count the number of "Beaver" in the list
print(animals.index("Panda"))  # index of the first "Panda" in the list
print(animals)