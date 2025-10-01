# Open the file 'menu.txt' in read mode ('r') using the 'with' statement
# 'with' ensures the file is automatically closed after we're done
with open("menu.txt", "r") as file:
    # Read each line in the file, remove any extra spaces or newlines, and store in a list called 'menu'
    menu = [line.strip() for line in file]

# Print a welcome message for the user
print("Welcome to the menu selector!")

# Prompt the user to select an item from the menu
print("Please select an item from the menu:")

# Loop through the 'menu' list and print each item with a number
# 'enumerate(menu, 1)' gives us both the position (starting from 1) and the menu item
for i, item in enumerate(menu, 1):
    # Print the number and menu item, formatted like "1. Cheeseburger"
    print(f"{i}. {item}")

# Start a loop that will keep running until the user selects a valid menu item
while True:
    try:
        # Ask the user to input a number corresponding to their menu choice
        # 'input()' takes user input as a string, and 'int()' converts it to a number
        choice = int(input("Enter the number of your selection: "))

        # Check if the user's choice is valid (between 1 and the number of menu items)
        if 1 <= choice <= len(menu):
            # If the choice is valid, print the selected menu item
            # 'menu[choice-1]' gets the item from the menu list (subtract 1 because lists start at 0)
            print(f"You selected: {menu[choice-1]}")
            # Exit the loop since the user made a valid selection
            break
        else:
            # If the number is outside the valid range, tell the user to try again
            print("Invalid selection. Please choose a number from the menu.")
    except ValueError:
        # If the user enters something that can't be converted to a number, show an error message
        print("Oops! You need to type a number.")
