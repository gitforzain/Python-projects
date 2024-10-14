print("Welcome TO Our Restaurant.")

print("Here Is Our Menu:")
print("1. Pizza : 200")
print("2. Pasta : 230")
print("3. Burger : 170")
print("4. Frize : 50")

menu = {
    "1": 200,   # Only store the prices
    "2": 230,
    "3": 170,
    "4": 50
}

order_names = {
    "1": "Pizza",
    "2": "Pasta",
    "3": "Burger",
    "4": "Frize"
}

# Initialize an empty list to store orders and their names
orders = []
order_total = 0

# Take the first order
order = input("Enter Your Order: ")
if order in menu:
    orders.append(order_names[order])
    order_total += menu[order]
else:
    print("Invalid Order.")

# Ask if the user wants to order more
again = input("Do You Want To Order More Things (Yes/No)? ").strip().lower()
if again == "yes":
    order1 = input("Enter Your Another Order: ")
    if order1 in menu:
        orders.append(order_names[order1])
        order_total += menu[order1]
    else:
        print("Invalid Order.")
else:
    print("No further orders.")

# Ask if the user wants to order even more
again2 = input("Do You Want To Order More Things (Yes/No)? ").strip().lower()
if again2 == "yes":
    order2 = input("Enter Your Another Order: ")
    if order2 in menu:
        orders.append(order_names[order2])
        order_total += menu[order2]
    else:
        print("Invalid Order.")
else:
    print("No further orders.")

# Display the orders and the total cost
if orders:
    print(f"Your orders are: {', '.join(orders)}")
    print(f"Total Cost: {order_total}")
else:
    print("You did not order anything available on the menu.")
