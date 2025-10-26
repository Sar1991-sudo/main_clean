# The following code should calculate the area of a rectangle based on the user inputs.

# Fix the example code below without altering defined function names or function parameters. Fixed code must produce similar results as is in the expected program runs. The code must also be fixed to match the requirements in the provided style guide


# Area = calculateArea()
# print("")
# print("Area is {Area}²")
# print("end")

# Expected program runs


# Program starting.
# Insert width: 2
def calculateArea(length, wigth):
   return length * wigth

def main():
    print("program starting")
    length = float(input("Insert length: "))
    width = float(input("Insert width: "))
    area = calculateArea(length, width)
    print(f"The area of the rectangle is: {area}")
    print("Program ending.")

main()

# Insert height: 3

# Area is 6.0²
# Program ending.
