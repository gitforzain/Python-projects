print("Welcome TO Our Restaurant.")

print("Here Is Our Menu:")
print("Pizza : 200")
print("Pasta : 230")
print("Burger : 170")
print("Frize : 50")

menu = {
    "Pizza": 200,
    "Pasta": 230,
    "Burger": 170,
    "Frize": 50
}

# Initialize the total cost and list of orders
total_cost = 0
orders = []

# Take the first order
order = input("Enter Your Order: ")
if order in menu:
    orders.append(order)
    total_cost += menu[order]
else:
    print("Sorry, the item is not available.")

# Ask if the user wants to order more
again = input("Do You Want To Order More Things (Yes/No)? ").strip().lower()
if again == "yes":
    order1 = input("Enter Your Another Order: ")
    if order1 in menu:
        orders.append(order1)
        total_cost += menu[order1]
    else:
        print("Sorry, the item is not available.")

# Ask if the user wants to order even more
again2 = input("Do You Want To Order More Things (Yes/No)? ").strip().lower()
if again2 == "yes":
    order2 = input("Enter Your Another Order: ")
    if order2 in menu:
        orders.append(order2)
        total_cost += menu[order2]
    else:
        print("Sorry, the item is not available.")

# Display the orders and the total cost
if orders:
    print(f"Your orders are: {', '.join(orders)}")
    print(f"Total Cost: {total_cost}")
else:
    print("You did not order anything available on the menu.")
