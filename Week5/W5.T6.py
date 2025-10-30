# Make a menu-driven Python program which mimics Tally Counter.

# This menu-driven program must contain a maintainable program structure with the following requirements:

# main function which represents the main program logic including menu cycle.
# showOptions function which takes no arguments, shows the available options in the standard output and returns None.
# askChoice function which takes no arguments, prompts user to insert choice and returns an integer regardless of the user feed.
# In case user incorrectly inserts text as a choice, the program must output "Unknown option!". For this, see the string method isnumeric() behaviour described in W3S or via Python documentation.

# See other requirements in the example program runs below.

# Example program runs


# Program starting.
# Options:
def showOptions():
    print("Menu:")
    print("1. Increase")
    print("2. Decrease")
    print("3. Reset")
    print("4. Show")
    print("5. Exit")
    return None

def askChoice():
    choice = input("Select an option (1-5): ")
    if choice.isnumeric():
        return int(choice)
    else:
        print("Unknown option!")
        return 0
    
def main():
    counter = 0

    while True:
        showOptions()
        choice = askChoice()
        print

        if choice == 1:
            counter += 1
        elif choice == 2:
            counter -= 1
        elif choice == 3:
            counter = 0
        elif choice == 4:
            print(f"Current count: {counter}\n")
        elif choice == 5:
            print("Exiting program...")
            break
        else:
            pass

print("Program ending.")
if __name__ == "__main__":
    main()      
# 1 - Show count
# 2 - Increase count
# 3 - Reset count
# 0 - Exit
# Your choice: 1
# Current count - 0

# Options:
# 1 - Show count
# 2 - Increase count
# 3 - Reset count
# 0 - Exit
# Your choice: 0
# Exiting program.

# Program ending.
