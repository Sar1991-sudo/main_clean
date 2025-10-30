# Write a Python program which asks user to insert hex color. In this case hex color is expected to be the 7 character representation starting with # and followed by 6 0-F characters to represent RGB colors. More about hex colors at https://en.wikipedia.org/wiki/Web_colors

# Slice the amount of red, green and blue from that inserted color and display each color as shown below.

# Example program run:

# Program starting.
print("Program starting.")

# Insert a hex color: #FFA500
hex_color = input("Insert a hex color: ")

# Colors
red = hex_color[1:3]
green = hex_color[3:5]
blue = hex_color[5:7]
# - Red FF
print(f"- Red {red}")
# - Green A5
print(f"- Green {green}")
# - Blue 00
print(f"- Blue {blue}")

# Program ending.
print("Program ending.")
