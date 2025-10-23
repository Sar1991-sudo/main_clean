# Prompt the user to insert the minutes spent on each previous topic task. Calculate the sum and the average. Display those in the example program run format(Note! precision). Make sure to calculate the required average for two decimal digits and later integer as rounded integer (precision 0 + type conversion).

# Example program run:

# Program starting.
print("Program starting.")
# Estimate how many minutes you spent on programming...
a1_t1 = int(input("A1_T1: "))
a1_t2 = int(input("A1_T2: "))
a1_t3 = int(input("A1_T3: "))
a1_t4 = int(input("A1_T4: "))
a1_t5 = int(input("A1_T5: "))
a1_t6 = int(input("A1_T6: "))
a1_t7 = int(input("A1_T7: "))

# A1_T1: 3
# A1_T2: 7
# A1_T3: 9
# A1_T4: 8
# A1_T5: 13
# A1_T6: 14
# A1_T7: 21

# In total you spent 75 minutes on programming.
total_time = a1_t1 + a1_t2 + a1_t3 + a1_t4 + a1_t5 + a1_t6 + a1_t7
print(f"In total you spent {total_time} minutes on programming.")
# Average per task was 10.71 min and same rounded to the nearest integer 11 min.
average_time = total_time / 7
print(f"Average per task was {round(average_time, 2)} min and same rounded to the nearest integer {round(average_time)} min.")


# Program ending.
print("Program ending.")
