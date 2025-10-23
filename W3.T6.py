# Create menu program with submenus. Mainly for unit conversions. Use the values from the following table for unit conversions https://www.isa.org/getmedia/192f7bda-c77c-480a-8925-1a39787ed098/CCST-Conversions-document.pdf

# Menu options:

# Length
# Meters to kilometers
# Kilometers to meters
# Weight
# Grams to pounds
# Pounds to grams
# Exit
# “Exiting...”
# Handle all the data in floating point datatype. Remember to round every value in 1 digit precision right before displaying.

# Other possible prints:

# “Unknown option.”
# Example run - weight conversion 1

# Program starting.
print("Program starting.")
# Welcome to the unit converter program!
print("Welcome to the unit converter program!")
# Follow the menu instructions below.


# Options: 
# 1 - Length
# 2 - Weight
# 0 - Exit
# Your choice: 1

# Length options:
print("Length options:")
# 1 - Meters to kilometers
print("1 - Meters to kilometers")
# 2 - Kilometers to meters
print("2 - Kilometers to meters")
# 0 - Exit
print("0 - Exit")
# Your choice: 1
Choice = int(input("Your choice: "))
if Choice == 1:
    amt = float(input("Insert meters: "))
    km = amt / 1000
    print(f"{amt:.1f} m is {km:.1f} km")
# Insert meters: 1000
elif Choice == 2:
    amt = float(input("Insert kilometers: "))
    m = amt * 1000
    print(f"{amt:.1f} km is {m:.1f} m")
# 1000.0 m is 1.0 km
elif Choice == 0:
    print("Exiting...")
else:
    print("Unknown option.")
# Program ending.
print("Program ending.")