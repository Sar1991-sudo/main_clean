print("program starting") 

value = int(input("Inserta positive integer: "))
rounds = 0

while value != 1:
    print(value, end=" ")
    if value % 2 == 0:
        value = value // 2
    else: 
        value = value * 3 + 1
    rounds += 1

print("1")
print(f"Sequnece had {rounds} total steps.")        
