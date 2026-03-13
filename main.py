# Import the necessary functions
from functions import register_sale, show_summary

print("=" * 50)
print("🛒 WELCOME TO THE SALES SYSTEM")
print("=" * 50)

# Validate customer name
customer_name = ""

while customer_name == "":
    customer_name = input("👤 Enter your name: ").strip()

    if customer_name == "":
        print("⚠ Name cannot be empty.")

# Validate customer ID
customer_id = ""

while customer_id == "":
    customer_id = input("🆔 Enter your ID number: ").strip()

    if customer_id == "":
        print("⚠ ID cannot be empty.")

print(f"\n✅ Welcome {customer_name}! You can now register sales.\n")

print("-" * 50)

# Ask how many sales the user wants to register
sales_valid = False

while sales_valid == False:
    try:
        sales_to_register = int(input("📦 How many sales would you like to register initially?: "))

        if sales_to_register < 0:
            print("⚠ Number cannot be negative.")
        else:
            sales_valid = True

    except ValueError:
        print("⚠ Please enter a valid number.")

print("\nStarting sales registration...\n")

# Register the initial number of sales
for i in range(sales_to_register):

    print(f"\n--- Registering sale #{i+1} ---")
    register_sale()

print("\nInitial sales completed.")
print("-" * 50)

# Option to continue registering sales
continue_register = "yes"

while continue_register == "yes":

    continue_register = input("\nDo you want to register another sale? (yes/no): ").lower()

    while continue_register != "yes" and continue_register != "no":
        print("⚠ Please type 'yes' or 'no'.")
        continue_register = input("Do you want to register another sale? (yes/no): ").lower()

    if continue_register == "yes":
        register_sale()

# Show summary
print("\n📊 Generating sales report...\n")

show_summary()
