# Make Python program which prompts user to insert two integers. Use these integers together with the “while-loop” structure to create behaviour like in the example program run below.

# Note! the autograding tool will test that the correct structure has been applied.

# Example program runs

# run 1 run 2 run 3

# Program starting.
print("Program starting.")

# Insert starting value: 1
Start = int(input("Insert starting value: "))
# Insert stopping value: 10
Stop = int(input("Insert stopping value: "))


# Starting while-loop:
while current <= Stop:
    if current == Stop:
        print(current)
    else:
        print(current, end=" ")
    current += 1
# 1 2 3 4 5 6 7 8 9 10

# Program ending.
print("Program ending.")