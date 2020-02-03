# Conditional Statements
# (if-else statements)

# Getting user input
# input(prompt) - atkes user input and returns as string

# Later (Error handling and validation)
age = int(input("Enter your age:"))
# or use     age = int(age)

if age >= 21:
    print("You can start drinking!")
elif 13 < age < 21:
    print("Study hard fot SAT!")
else:
    print("Play video games!")