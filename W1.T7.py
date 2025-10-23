# Create a Python program that is able to calculate car’s fuel consumption (diesel or petrol) and present the consumption in liters per 100km “x l per 100 km”

# Print info message “Calculate fuel consumtion.”
print("Calculate fuel consumption.")
# Ask “Enter travel distance(kilometers): ” and store the value to Feed variable
Feed = input("Enter travel distance(kilometers): ")
Distance = int(Feed)
# Convert the Feed into an integer and assign it to Distance variable
# Ask “Enter fuel usage(liters): ”
Feed = input("Enter fuel usage(liters): ")
FuelUsage = int(Feed)
# Convert the Feed into an integer and assign it to FuelUsage variable


# Calculate the Consumption for 100 km
Consumption = (FuelUsage / Distance) * 100
# Convert the Consumption back to an integer
# Print “Fuel consumption is {Consumption} l per 100 km”
print(f"Fuel consumption is {int(Consumption)} l per 100 km")


# Calculate fuel consumption.
# Enter travel distance(kilometers): 200
# Enter fuel usage(liters): 20
# Fuel consumption is 10 l per 100 km
