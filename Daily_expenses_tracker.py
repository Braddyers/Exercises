print("Welcome to the Daily Expense Tracker!\n")

# Display menu once
print("\nMenu:")
print("1. Add a new expense")
print("2. View all expenses")
print("3. Calculate total and average expense")
print("4. Clear all expenses")
print("5. Exit")

while True:
    
    menu_input = input()

    if menu_input == "5":
        print("Exiting the Daily Expense Tracker. Goodbye!")
        break
