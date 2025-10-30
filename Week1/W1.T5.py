# Make a Python program which can take user inputs and convert them into integers.

# Print “Calculate the area of a wall.”
# Prompt user
# “Enter the width in meters: ”
# Store the input value into Feed variable.
# Convert the Feed variable into an integer and store it in Width variable
# Prompt user
# “Enter the height in meters: ”
# store the input value into Feed variable.
# Convert the Feed variable into an integer and store it in Height variable
# Print “Width is {Width} m and height is {Height} m.”
# Multiply Width and Height, then store the result in Area variable
# Display results to the user: “The wall will be {Area} square meters.”
# Try the program with different inputs e.g. decimals. Notice any problems in the program? Are you able to solve the issue?

# The test environment(GitHub Classroom) may run your code multiple times with different integer values.

# Example program run:

# Calculate the area of a wall.
print("Calculate the area of a wall.")
# Enter the width in meters: 2
Feed = input("Enter the width in meters: ")
Width = int(Feed)
# Enter the height in meters: 3
Feed = input("Enter the height in meters: ")
Height = int(Feed)
# Width is 2 m and height is 3 m.
print(f"Width is {Width} m and height is {Height} m.")
Area = Width * Height
# The wall will be 6 square meters.
print(f"The wall will be {Area} square meters.")

