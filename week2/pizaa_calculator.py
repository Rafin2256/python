# Function to calculate the total cost of the pizza order including tax
def calculate_total_cost(num_pizzas, pizza_cost):
    # Calculate the subtotal
    subtotal = num_pizzas * pizza_cost
    # Calculate the sales tax (20% of the subtotal)
    sales_tax = subtotal * 0.20
    # Calculate the final total (subtotal + sales tax)
    total_cost = subtotal + sales_tax
    return subtotal, sales_tax, total_cost

# Ask the user for the number of pizzas
num_pizzas = int(input("Enter the number of pizzas you'd77 like to order: "))

# Ask the user for the cost of one pizza
pizza_cost = float(input("Enter the cost of a single pizza: "))

# Call the function to calculate the subtotal, tax, and total
subtotal, sales_tax, total_cost = calculate_total_cost(num_pizzas, pizza_cost)

# Display the subtotal, sales tax, and total cost
print(f"\nSubtotal: £{subtotal:.2f}")
print(f"Sales Tax (20%): £{sales_tax:.2f}")
print(f"Total Cost (including tax): £{total_cost:.2f}")
