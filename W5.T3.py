# Create a Python program with two functions:

# main-function
# Does the routines ("Program starting." and "Program ending.")
# Utilizes askName-function.
# Utilizes greetUser-function.
# Returns None
# askName-function
# Prompts the user to insert name
# Returns name
# greetUser-function
# Which takes PName as an argument
# Greets the user "Hello {PName}!"
# Returns None
# Note! Tests for this task relies on properly defined functions and may fail if the program is not written according to the instructions.


# Program starting.
def askName():
    name = input("Insert name: ")
    return name

def greetUser(PName):
    print(f"Hello {PName}!")
    return None

def main():
    print("Program starting")
    print()
    user_name = askName()
    greetUser(user_name)
    print()
    print("Program ending")
    return None
main()
# Insert name: John
# Hello John!
# Program ending.
