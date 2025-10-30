# Make a Python program, which prompts the user name and two floating numbers. Multiply the inserted numbers to get product. Round the product in two decimal precision. Complete the program output as shown below.


# Program starting.
print("Program starting.")
# What is your name: John
name = input("What is your name: ")
# Enter a floating point number: 3.1
first_number = float(input("Enter a floating point number: "))
# Enter second floating point number: 5.3
second_number = float(input("Enter second floating point number: "))
# John you gave numbers 3.1 and 5.3
print(f"{name} you gave numbers {first_number} and {second_number}")
# Multiplying first and second number will result in product 16.43
product = first_number * second_number
# Program ending.
print(f"Multiplying first and second number will result in product {round(product, 2)}")
