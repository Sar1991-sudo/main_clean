print("program satarting")
print("")
Feed = input("insert starting ponit: ")
Pointstart = int(Feed)
Feed = input("insert stopping point: ")
Pointstop = int(Feed)
Feed = input("insert inspection point: ")
Pointinspect = int(Feed)
print("")

Run = True

if(PointStart >= PointStop):
    print("starting point value must be less than stopping point value.")
    Run = false
if((Pointstart > PointInspect) or (PointInspect > PointStop)):
    print("inspection value must be within the range of start and stop.")  
    Run = false

if(Run):
    print("first loop - inspection with break:") 
    for i in range(PointStart, PointStop):
        if(i == Pointinspect):
            break
        else:
            print(i, end=' ')
    print("")
    print("second loop - inspection with continue:")
    for i in range(PointStart, PointStop) 
        if(i == Pointinspect):
            continue
        else:
            if(i == (PointStop-1)):
            print(i)
        else:
            print(i, end=' ') 


    print("program ending")  