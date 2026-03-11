# List that stores all the sales registered during the program execution
sales = []

def register_sale():
    """
    This function registers a new sale.
    It asks the user for the product name, unit price and quantity sold.
    It also validates the inputs to prevent errors.
    """

    # Validate product name (cannot be empty)
    while True:
        product = input("Enter product name: ").strip()

        if product == "":
            print("Product name cannot be empty.")
        else:
            break

    # Validate unit price (must be a number)
    while True:
        try:
            price = float(input("Enter unit price: "))

            # Prevent negative prices
            if price < 0:
                print("Price cannot be negative.")
                continue

            break

        except ValueError:
            # This error occurs if the user enters text instead of a number
            print("Invalid input. Please enter a numeric value.")

    # Validate quantity sold (must be an integer)
    while True:
        try:
            quantity = int(input("Enter quantity sold: "))

            # Prevent negative quantities
            if quantity < 0:
                print("Quantity cannot be negative.")
                continue

            break

        except ValueError:
            # Error if the user enters something that is not an integer
            print("Invalid input. Please enter a whole number.")

    # Calculate the total value of the sale
    total = price * quantity

    # Create a dictionary to store the sale information
    sale = {
        "product": product,
        "price": price,
        "quantity": quantity,
        "total": total
    }

    # Add the sale dictionary to the sales list
    sales.append(sale)


def calculate_totals():
    """
    This function processes all the sales stored in the list.
    It calculates:
    - The total quantity sold for each product
    - The total revenue of the day
    """

    # Dictionary that will store the total quantity sold per product
    product_summary = {}

    # Variable that accumulates the total revenue
    total_revenue = 0

    # Loop through each sale stored in the sales list
    for sale in sales:

        # Extract information from the sale dictionary
        product = sale["product"]
        quantity = sale["quantity"]
        total = sale["total"]

        # Add the sale total to the daily revenue
        total_revenue += total

        # Check if the product already exists in the summary dictionary
        if product in product_summary:

            # If it exists, add the quantity to the previous quantity
            product_summary[product] += quantity

        else:
            # If it does not exist, create a new entry
            product_summary[product] = quantity

    # Return the summary dictionary and the total revenue
    return product_summary, total_revenue


def show_summary():
    """
    This function displays the final sales report.
    It calls the calculate_totals() function and prints
    the products sold and the total revenue.
    """

    # Call the function that calculates totals
    product_summary, total_revenue = calculate_totals()

    # Print the title of the summary
    print("\nSALES SUMMARY OF THE DAY\n")

    # Loop through each product in the summary dictionary
    for product, quantity in product_summary.items():

        # Print product information
        print("Product:", product)
        print("Total quantity sold:", quantity)
        print()

    # Print the total revenue generated during the day
    print("Total revenue: $", total_revenue)