# Copy the previous program and modify the behaviour to match the example program run below. This program must use “for-loop” structure.

# It is recommended to replace the print-command end character with space, so that all the iterations can be printed on the same row. Last iteration might require additional logic to get rid of the extra space at the end.

# Note! the autograding tool will test that the correct structure has been applied.

# Example program runs

# run 1 run 2 run 3

# Program starting.
print("Program starting.")

# Insert starting value: 11
satart = int(input("Insert starting value: "))
# Insert stopping value: 15
stop = int(input("Insert stopping value: "))

# Starting for-loop:
for i in range(satart, stop + 1):
    if i == stop:
        print(i)
    else:
        print(i, end=' ')
      # To ensure the next print starts on a new line
# 11 12 13 14 15

# Program ending.
print("Program ending.")
