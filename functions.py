# List that stores all the sales registered during the program execution
sales = []

def register_sale():
    """
    Register a new sale with validation.
    """

    print("\n📝 Register a new sale")
    print("-" * 30)

    # Validate product name
    product = ""
    while product == "":
        product = input("Enter product name: ").strip()

        if product == "":
            print("⚠ Product name cannot be empty.")

    # Validate unit price
    price_valid = False

    while price_valid == False:
        try:
            price = float(input("Enter unit price: "))

            if price < 0:
                print("⚠ Price cannot be negative.")
            else:
                price_valid = True

        except ValueError:
            print("⚠ Invalid input. Please enter a numeric value.")

    # Validate quantity
    quantity_valid = False

    while quantity_valid == False:
        try:
            quantity = int(input("Enter quantity sold: "))

            if quantity < 0:
                print("⚠ Quantity cannot be negative.")
            else:
                quantity_valid = True

        except ValueError:
            print("⚠ Invalid input. Please enter a whole number.")

    total = price * quantity

    sale = {
        "product": product,
        "price": price,
        "quantity": quantity,
        "total": total
    }

    sales.append(sale)

    print("✅ Sale registered successfully!")


def calculate_totals():
    """
    Calculate total quantity per product and total revenue.
    """

    product_summary = {}
    total_revenue = 0

    for sale in sales:

        product = sale["product"]
        quantity = sale["quantity"]
        total = sale["total"]

        total_revenue += total

        if product in product_summary:
            product_summary[product] += quantity
        else:
            product_summary[product] = quantity

    return product_summary, total_revenue


def show_summary():
    """
    Display the sales summary.
    """

    product_summary, total_revenue = calculate_totals()

    print("=" * 40)
    print("📊 SALES SUMMARY OF THE DAY")
    print("=" * 40)

    for product, quantity in product_summary.items():

        print(f"Product: {product}")
        print(f"Total quantity sold: {quantity}")
        print("-" * 20)

    print(f"\n💰 Total revenue: ${total_revenue}")

    
