# Errors

# 1. Syntax Error (Compile-time Error)
# - when Python cannot interpret your code, since you didn't follow
#   the correct syntax for Python.
# - These errors you're likely to get when you make a typo (indentation)
# - Pycharm will show red underline


# 2. Exceptions (Run-time Error) = crash
# - When unexpected thins happen during the execution of a program (run-time),
#   even if your code is syntactically correct.
# - There are different types of Exceptions in Python, and you can
#   see which exception is 'thrown (raised)' in the error message.
# --> PLEASE READ THE ERROR MESSAGE!

while True:
    try:
        # ValueError
        a = int(input("Enter a number: "))
        b = int(input("Enter a number: "))
        c = a / b
        print(c)
        break
    except ValueError as err:
        print(f"Invalid input: {err}")
        print("Please enter a number")
    except ZeroDivisionError:
        print("Cannot divide by zero.")
        print("Please enter a non-zero number")
    except KeyboardInterrupt:
        # KeyboardInterrupt: ctrl + c
        print("\nNo input taken.\n")
    except EOFError as e:
        # EOF: ctrl + d  (end of file)
        print(f"{e}")
    finally:
        # Always run at the end
        print("All Done!!")



# NEXT WEEK

# Search
# - Linear Search
# - Binary Search

# ================= (for loop)
# Sorting
# - Bubble Sort
# - Selection Sort
# - Insertion Sort

# Recursion + Sort
# - Merge Sort

# Primes
# GreatestCommomDivisor (GCD)
# LeasCommonMultiples (LCM)
