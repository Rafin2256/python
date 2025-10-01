import os

# Function to read the list of books from the file
def read_file_list():
    """Reads the books from books.txt and returns them in a stack."""
    file_stack = []  # Initialize an empty stack (list) for books
    if os.path.exists('books.txt'):  # Check if the file exists
        with open('books.txt', 'r') as file:  # Open the file in read mode
            for line in file:  # Read each line in the file
                file_stack.append(line.strip())  # Add the book title to the stack, removing extra spaces
    return file_stack  # Return the stack of books

# Function to update the file with the current stack of books
def update_file_list(stack):
    """Writes the updated stack to books.txt."""
    with open('books.txt', 'w') as file:  # Open the file in write mode
        for book in stack:  # Loop through each book in the stack
            file.write(f"{book}\n")  # Write the book title to the file, adding a new line

# Main function to manage the book shop
def main():
    """Main program loop."""
    stack = read_file_list()  # Initialize the stack by reading from the file

    while True:  # Start an infinite loop for the menu
        # Display the menu options
        print("\n=== Book Queue Manager ===")
        print("1. Add book")
        print("2. Remove last book")
        print("3. Remove first book")
        print("4. View all books")
        print("5. Exit")

        choice = input("\nWhat would you like to do? (1-5): ")  # Get user input

        if choice == '1':  # Option to add a book
            book = input("Enter book title: ")  # Ask the user for the book title
            stack.append(book)  # Add the book to the stack
            update_file_list(stack)  # Update the file with the new stack
            print(f"Added '{book}' to the stack")

        elif choice == '2':  # Option to remove the last book
            if stack:  # Check if the stack is not empty
                book = stack.pop()  # Remove the last book from the stack
                update_file_list(stack)  # Update the file with the new stack
                print(f"Removed '{book}' from the top")
            else:  # If the stack is empty
                print("Stack is empty!")

        elif choice == '3':  # Option to remove the first book
            if stack:  # Check if the stack is not empty
                book = stack.pop(0)  # Remove the first book from the stack
                update_file_list(stack)  # Update the file with the new stack
                print(f"Removed '{book}' from the bottom")
            else:  # If the stack is empty
                print("Stack is empty!")

        elif choice == '4':  # Option to view all books
            if stack:  # Check if the stack is not empty
                print("\nCurrent stack of books (top to bottom):")
                for index, book in enumerate(stack):  # Loop through the stack with index
                    print(f"{index + 1}. {book}")  # Display each book with its position
            else:  # If the stack is empty
                print("Stack is empty!")

        elif choice == '5':  # Option to exit the program
            print("Goodbye!")  # Say goodbye to the user
            break  # Exit the loop

        else:  # If the user enters an invalid option
            print("Invalid choice! Please enter a number between 1-5.")

# Check if this script is being run directly
if __name__ == "__main__":
    main()  # Run the main function
