# Make a program, which prompts user to insert words. Program must stop prompting words if user inserts empty word. After stopping the repetitive prompt, print the amount of words and characters that the user inserted.

# Example program run:

# run 1 run 2 run 3
# Program starting.
print("Program starting.")

# Insert word (empty stops): Close
word_count = 0
char_count = 0
# Insert word (empty stops): the
while True:
    word = input("Insert word (empty stops): ")
    if word == "":
        break
    word_count += 1
    char_count += len(word)

# Insert word (empty stops): loop 
# Insert word (empty stops): 


# You inserted:
print(f"- {word_count} words")
print(f"- {char_count} characters")
# - 3 words
# - 12 characters


# Program ending.
print("Program ending.")
