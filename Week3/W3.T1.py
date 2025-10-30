# Make Python program and implement if-statements in proper places.

# Ask user to insert two integers
# Compare the integers and then announce the greater number
# Create sum of the two integers
# Check the parity of the sum (see modulo-operator ‘%’)
# Other possible output variants:

# Integer comparison
# Integers are the same.
# First integer is greater.
# Parity check
# Sum is even.


# Program starting.
print("Program starting.")
# Insert two integers.
print("Insert two integers.")
# Insert first integer: 5
Int1 = input("Insert first integer: ")
# Insert second integer: 5
Int2 = input("Insert second integer: ")
# Comparing inserted integers.
print("Comparing inserted integers.")
if(Int1 > Int2):
    print("First integer is greater.")
elif(Int2 > Int1):
    print("Second integer is greater.")
else:    
    print("Integers are the same.")

print("")
    # First integer is greater.


# Adding integers together
Sum = int1 + int2

# 5 + 5 = 10
print(f"{Int1} + {Int2} = {Sum}")


# Checking the parity of the sum...
if sum_of_integers % 2 == 0:
    print("Sum is even.")
else:
    print("Sum is odd.")

# Sum is even.

# Program ending.
print("Program ending.")
