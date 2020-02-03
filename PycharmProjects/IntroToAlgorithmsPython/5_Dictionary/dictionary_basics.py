# list, strings, tuples are index-based (0, 1, 2, 3,......)

# Dictionary: A collection of key-value pairs
# (Some other languages they call it "Map")
# * You access its values by looking up a "key" instead of an index
# * keys MUST be UNIQUE. (A key can be any string or number)

contacts = {
    "Cayo": "778-123-1234",
    "Martin": "778-321-4312",
    "Derrick": "778-392-4838"
}

# Acess dictionary to get value
print(contacts["Cayo"])

# Add a new entry (key-value pair)

contacts["Leo"] = "604-198-2348"
print(contacts)

# Update a value for existing key
contacts["Leo"] = "No Phone Number"
print(contacts)

# Delete an entry from dictionary
del contacts["Martin"]
print(contacts)

# Get a list of all the keys
key_list = list(contacts.keys())
print(key_list)
val_list = list(contacts.values())
print(val_list)

# `in` keyword
# The `in` keyword is used to check if a list or dictionary contains a specific key.

print("John" in contacts)
print("Leo" in contacts)
