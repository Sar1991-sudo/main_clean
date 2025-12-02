print("Program starting.\n")

print("Check multiplicative persistence.")
n = int(input("Insert an integer: "))

step = 0

while n >= 10:
    step += 1
    digits = [int(d) for d in str(n)]
    product = 1
    for d in digits:
        product *= d

    calc_str = " * ".join(str(d) for d in digits)
    print(f"{step}: {calc_str} = {product}")

    n = product

print("No more steps.\n")
print(f"This program took {step} step(s)\n")
print("Program ending.")
