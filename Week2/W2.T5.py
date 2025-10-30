# Make a Python program, which prompts for a compound word.

# Get following aspects from the word
# Length
# First character
# Reversed version e.g. “Suitcase” is reversed “esactiuS”
# Display the aspects using print commands.
# Prompt the user to take substring from the existing compound word.
# Finally print the user specified substring.
# Example program run:

# Program starting.
print("Program starting.")

# Insert a closed compound word: Moonbanana
compound_word = input("Insert a closed compound word: ")
# The word you inserted is 'Moonbanana' and in reverse it is 'ananabnooM'.
reversed_word = compound_word[::-1]
print(f"The word you inserted is '{compound_word}' and in reverse it is '{reversed_word}'.")
# The inserted word length is 10
print(f"The inserted word length is {len(compound_word)}")
# Last character is 'a'
print(f"Last character is '{compound_word[-1]}'")


# The word 'Moonbanana' sliced to the defined substring is 'Moon'.
start_index = int(input("Starting point: "))
end_index = int(input("Ending point: "))
step_size = int(input("Step size: "))
substring = compound_word[start_index:end_index:step_size]
print(f"The word '{compound_word}' sliced to the defined substring is '{substring}'.")
# Program ending.
print("Program ending.")
