# Make Python program which does the following steps:

# Prompt user to insert
# A word
# A character
# Find if the character exists in the word. Possible prints below.
# Word "{WordFirst}" contains character "{Character}"
# Word "{WordFirst}" doesn't contain character "{Character}"
# Prompt user to insert one more word
# Compare the first word to the second word. Examples below:
# The first word "{WordFirst}" is before the second word "{WordSecond}" alphabetically.
# The second word "{WordSecond}" is before the first word "{WordFirst}" alphabetically.
# Both inserted words are the same alphabetically, "{WordFirst}"
# Example program run


# Program starting.
print("Program starting.")
# String comparisons
print("String comparisons")
# Insert first word: beans
first_word = input("Insert first word: ")
# Insert a character: n
character = input("Insert a character: ")
# Word "beans" contains character "n"
if character in first_word:
    print(f'Word "{first_word}" contains character "{character}"')
else:
    print(f'Word "{first_word}" doesn\'t contain character "{character}"')
# Insert second word: banana
second_word = input("Insert second word: ")
# The second word "banana" is before the first word "beans" alphabetically.
if first_word < second_word:
    print(f'The first word "{first_word}" is before the second word "{second_word}" alphabetically.')
elif second_word < first_word:
    print(f'The second word "{second_word}" is before the first word "{first_word}" alphabetically.')
else:
    print(f'Both inserted words are the same alphabetically, "{first_word}"')
# Program ending.
print("Program ending.")

