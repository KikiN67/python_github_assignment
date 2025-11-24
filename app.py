# Water Intake Monitor
# This program is designed to help users track their daily water intake and see how much more they need to drink to reach their goal. 
print("Welcome to my Python program!")
# Step 1: Welcome message
print("welcome to the Water Intake Monitor!")

# Step 2: Ask user for input

glasses = input("How many glasses of water have you drank today?")

# step 3: Convert input and handle errors

try:
    glasses = float(glasses) # Convert input to a numberic value 
except ValueError:
    print("Oops! Please enter a valid number.")
    exit() # Stop the program if invalid input is entered

# Step 4: Perform calculation

ounces_per_glass = 8
total_ounces = glasses * ounces_per_glass

# step 5: Display results

daily_goal = 40 # Recommended daily water intake in ounces
print(f"\nYou have consumed {total_ounces} ounces of water today.")

# Step 6: Final decision & message based on progress
if total_ounces >= daily_goal:
    print(f"YOU DID IT! CONGRATULATIONS! You drank {glasses} glasses of water today. You hit your water goal for today!")
else:
    # how many more ounces/glasses needed
    ounces_needed = daily_goal - total_ounces
    glasses_needed = ounces_needed / ounces_per_glass
    print(f"Keep going! You only need {glasses_needed:.1f} more glasses to reach your goal. Keep working hard and drinking that water!")
