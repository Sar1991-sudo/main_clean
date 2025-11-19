print("Program starting.")

start = int(input("Insert starting point: "))
stop = int(input("Insert stopping point: "))
inspect = int(input("Insert inspection point: "))

if start >= stop:
    print("Starting point value must be less than the stopping point value.")
elif not (start <= inspect <= stop):
    print("Inspection value must be within the range of start and stop.")
else:
    print("First loop- inspection with break:")
    first = True
    for i in range(start, stop):
        if i == inspect:
            break
        if not first:
            print("・", end="")
        print(i, end="")
        first = False
    print()

    print("Second loop - inspection with continue:")
    first = True
    for i in range(start, stop):
        if i == inspect:
            continue
        if not first:
            print("・", end="")
        print(i, end="")
        first = False
    print()

print("Program ending.")
