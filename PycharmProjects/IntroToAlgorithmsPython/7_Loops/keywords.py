# Debug? - `De`bug
# - Debugger: `break point`


# `break` statement: stop!
# - break out of the loop!

#ex) print numbers from a list if there's a 4 stop printing.
items = [12, 1, 5, 4, 16, 21, 6, 3, 8, 7]

for item in items:
    if item == 4:
        break
    print(item)

# `continue` statement: skip!
# - skip to the next iteration

for item in items:
    if item == 4:
        continue
    print(item)