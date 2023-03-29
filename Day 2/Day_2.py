# Get the total bill from the user
bill = float(input("What was the total bill? "))

# Get the tip percentage from the user
tip = int(input("What amount would you like to tip, 10, 12 or 15? "))

# Get the number of people splitting the bill from the user
people = int(input("How many people will split the bill? "))

# Calculate the total tip amount
total_tip = bill * (tip / 100) / people

# Print the total tip amount
print(f"${round(total_tip, 2)} tip")