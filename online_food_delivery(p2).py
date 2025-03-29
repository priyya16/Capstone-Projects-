import random

menu = {
    "Burger": (120, "Fast Food"),
    "Pizza": (250, "Fast Food"),
    "Pasta": (180, "Italian"),
    "Salad": (100, "Healthy"),
    "Sandwich": (150, "Fast Food"),
    "Juice": (90, "Beverage")
}

orders = []
customers = set()

def display_menu():
    print("\nMenu:")
    for item, (price, category) in menu.items():
        print(f"{item} - Rs.{price} ({category})")

def place_order():
    order_id = random.randint(1000, 9999)
    customer_name = input("\nEnter your name: ")
    customers.add(customer_name)
    
    item_list = []
    total_bill = 0

    while True:
        display_menu()
        item = input("\nEnter item name to order (or type 'done' to finish): ").strip()
        if item.lower() == "done":
            break
        if item in menu:
            item_list.append(item)
            total_bill += menu[item][0]
        else:
            print("Invalid item, please select from the menu.")

    if item_list:
        orders.append((order_id, customer_name, item_list, total_bill))
        print(f"\nOrder placed successfully! Order ID: {order_id}")
        print(f"Total Bill: Rs.{total_bill}")

def total_revenue():
    revenue = sum(order[3] for order in orders)
    print(f"\nTotal Revenue: Rs.{revenue}")

def unique_customers():
    print("\nUnique Customers who placed orders:")
    for customer in customers:
        print(customer)

while True:
    print("\n1. Place Order\n2. View Total Revenue\n3. View Unique Customers\n4. Exit")
    choice = input("Enter your choice: ")

    if choice == "1":
        place_order()
    elif choice == "2":
        total_revenue()
    elif choice == "3":
        unique_customers()
    elif choice == "4":
        print("Exiting...")
        break
    else:
        print("Invalid choice, please try again.")
