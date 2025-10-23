# Create a Python program that is able to calculate remainder. Remainder can be calculated using modulo “%” operator. See also “modulus” example in W3Schools.

# Prompt user “Insert an integer: ” and assign the input value into Feed variable
# Convert the Feed into an integer and assign it to Value variable
# Calculate the remainder of the Value when divided by 2 and assign it to the Remainder variable.
# Print the inserted value “Value is {Value}”
# Print the remainder value “The remainder is {Remainder} when {Value} is divided by 2.”
# Example program run:

# Insert an integer: 479
Feed = input("Insert an integer: ")
Value = int(Feed)
# Value is 479
Remainder = Value % 2
print(f"Value is {Value}")
# The remainder is 1 when 479 is divided by 2.
print(f"The remainder is {Remainder} when {Value} is divided by 2.")
