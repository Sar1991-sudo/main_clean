# Create a Python program which collects words in a collectWords-function and analyses the words in a analyseWords-function. Use main-function to define the main logic.

# Main logic

# Call the collectWords-function and store the words into a local variable. Next pass the collected words to the analyseWords-function.

# Prompt user to insert word. Repeat the prompt till the user enters an empty word. Collect all words into one variable where each word is separated by a DELIMITER. At the end of the function, return the string variable holding all of the words.

# Takes one parameter containing words wrapped into one string. Calculates the amount of words, characters and the average word length. Separating words must happen by utilizing the DELIMITER. Finally displays the results. Average word length must be presented in 2 decimal precision. This function should not return anything.

# Use print("- {:.2f} Average word length".format(Avg)) to print average word length in 2 decimal precision.

# Example program runs


# Program starting.
# Insert word(empty stops): change
# Insert word(empty stops): is
# Insert word(empty stops): constant
# Insert word(empty stops): 
# - 3 Words
# - 16 Characters
# - 5.33 Average word length
# Program ending.


DELIMITER = ","

def collectWords():
    words = []
    while True:
        word = input("Insert word (empty stops) ")
        if word == "":
            break
        words.append(word)
    return DELIMITER.join(words)    
    
def analysWords(words):
    if words =="":
        word_list = []
    else:
        word_list = words.split(DELIMITER)

    word_count = len(word_list)
    char_count = sum(len(word) for word in word_list)  

    avg_length = char_count / word_count if word_count > 0 else 0.0

    print(f"-{word_count} words")
    print(f"-{char_count}characters")
    print("- {:.2f} Average word length".format(avg_length)) 


def main():
    print("Program starting.")
    words = collectWords()
    analysWords(words)
    print("Program ending.")

if __name__ == "__main__":
    main()
