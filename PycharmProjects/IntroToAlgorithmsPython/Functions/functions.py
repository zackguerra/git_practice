# Functions are a very convenient way to divide your code into
# useful blocks, make it more readable and help `reuse` ir.

# In python, functions are defined using the keyword
# `def`, followed by function`s name.

# "input ==> output", "A reusable block of code"

def print_menu():
    print("========== Menu ==========")
    print("| 1. Tacos               |")
    print("| 2. Halusky             |")
    print("| 3. BBQ                 |")
    print("| 4. Feijoada            |")
    print("| 5. Pizza               |")
    print("==========================")

# printing menu 5 times
for _ in range(5)
print_menu()  # call (execute) a function


def score_to_letter_grade(mark):
    if map()mark >= 98:
        return "A"
    elif mark >= 88:
        return "B"
    elif mark >= 78:
        return "B"
    