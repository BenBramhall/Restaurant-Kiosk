print('Welcome to West Shark Cafe!')
print('Our Menu: Coffee, Mocha, Red Bull')

menu = {
    "Coffee": 5.0,
    "Mocha": 3.5,
    "Red Bull": 3.0
}

orders = []
total_to_add = 0

while True:
    choice = input("\nType a menu item to add, 'remove' to delete something, or 'done' to quit: ").strip().title()

    if choice == "Done":
        print('Shutting Down...')
        break

    if choice == "Remove":
        if not orders:
            print("Your order is empty.")
            continue
        item_to_remove = input("What would you like to remove? ").strip().title()
        if item_to_remove in orders:
            orders.remove(item_to_remove)
            # Subtract the price
            total_to_add -= menu.get(item_to_remove, 0)
            print(f"{item_to_remove} removed.")
            print("Current order:", orders)
        else:
            print("This item is not in your order.")
        continue

    # Add item
    if choice in menu:
        price = menu[choice]
        total_to_add += price
        orders.append(choice)
        print(f"Added {choice} → ${price:.2f} | Running Total: ${total_to_add:.2f}")
    else:
        print("Sorry, that's not on the menu.")

print("\nFinal Order:", orders)
print(f"Final Total: ${total_to_add:.2f}")