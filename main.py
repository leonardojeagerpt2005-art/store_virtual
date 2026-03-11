# Import the necessary functions from the functions file
from functions import register_sale, show_summary

# Welcome message for the user
print("Welcome to our store. Please enter your information to continue.")

# Validate customer name
customer_name = ""

while customer_name == "":
    customer_name = input("Enter your name: ").strip()

    if customer_name == "":
        print("Name cannot be empty.")

# Validate customer ID
customer_id = ""

while customer_id == "":
    customer_id = input("Enter your ID number: ").strip()

    if customer_id == "":
        print("ID cannot be empty.")

# Confirmation message
print(f"Thank you {customer_name}. You can now proceed with the purchase.")

# Variable that controls the sales registration loop
continue_register = "yes"

# Loop that allows registering multiple sales
while continue_register == "yes":

    # Call the function that registers a new sale
    register_sale()

    # Ask the user if they want to continue
    continue_register = input("Do you want to register another sale? (yes/no): ").lower()

    # Validate the response
    while continue_register != "yes" and continue_register != "no":
        print("Please type 'yes' or 'no'.")
        continue_register = input("Do you want to register another sale? (yes/no): ").lower()

# After finishing the sales registration, display the summary
show_summary()
