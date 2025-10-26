# Create a menu-driven Python program with following options:

# Insert a word
# Which stores user inserted word into memory.
# Show current word
# Prints the word from the memory
# Show current word in reverse
# Prints the word from the memory in reverse.
# Exit
# Stops the program gracefully
# Unknown option
# Initialize the Word with an empty string.

# Example program runs

# Program starting.
# Options:
def main():
    print("Program starting")
    print()
    
word = ""

while True:
    print("Menu:")
    print("1. Insert a word")
    print("2. Show current word")
    print("3. Show current word in reverse")
    print("4. Exit")


    choice = input("Select an option (1-4): ")
    print()
    if choice == "1":
        word = input("Insert a word: ")
        print("Word saved.\n")
    elif choice == "2":
        print(f"Current word: {word}\n") 
    elif choice == "3":
        print(f"Word in reverse: {word[::-1]}\n")
    elif choice == "4":
        print("Exiting program...")
        break
    else:
        print("Unknown opition.\n")

print("Program ending.")
if __name__ == "__main__":
    main()



# 1 - Insert word
# 2 - Show current word
# 3 - Show current word in reverse
# 0 - Exit
# Your choice: 1
# Insert word: Banana

# Options:
# 1 - Insert word
# 2 - Show current word
# 3 - Show current word in reverse
# 0 - Exit
# Your choice: 2
# Current word - "Banana"

# Options:
# 1 - Insert word
# 2 - Show current word
# 3 - Show current word in reverse
# 0 - Exit
# Your choice: 3
# Word reversed - "ananaB"

# Options:
# 1 - Insert word
# 2 - Show current word
# 3 - Show current word in reverse
# 0 - Exit
# Your choice: 0
# Exiting program.

# Program ending.
