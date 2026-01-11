def collatz_sequence(n: int)-> list[int]:
    sequence = [n]
    while n != 1:
        if n % 2 == 0:
            n //= 2
        else:
            n = 3 * n + 1
        sequence.append(n)
    return sequence

def main():
    print("Program starting")
    try:
        num = int(input("Insert a positive integer. "))
        if num <= 0:
            print("Please insert a positive integer greater than 0.")
            return 
    expect ValueError:
        print("Invalid input. Please enter a positive integer.")
        return
    seq = collatz_sequence(num)
    print("->".join(map(str, seq)))
    steps = len(seq) -1
    print(f"Sequence had {steps} total steps.\n")
    print("Program ending.")
if __name__=="__main__":
    main()
