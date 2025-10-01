# Initialise an empty stack for books
stack = []

while True:
    print("\n=== Book Queue Manager ===")
    print("1. Add book")
    print("2. Remove last book")
    print("3. Remove first book")
    print("4. View all books")
    print("5. Exit")
    
    choice = input("\nWhat would you like to do? (1-5): ")
    
    if choice == '1':  # Add a book
        book = input("Enter book title: ")
        stack.append(book)  # Append the book to the stack
        print(f"Added '{book}' to the stack.")
    
    elif choice == '2':  # Remove the last book
        if stack:
            removed_book = stack.pop()  # Remove the last book from the stack
            print(f"Removed '{removed_book}' from the end.")
        else:
            print("Stack is empty! Nothing to remove.")
    
    elif choice == '3':  # Remove the first book
        if stack:
            removed_book = stack.pop(0)  # Remove the first book from the stack
            print(f"Removed '{removed_book}' from the start.")
        else:
            print("Stack is empty! Nothing to remove.")
    
    elif choice == '4':  # Display all books
        if stack:
            print("\nCurrent stack of books:")
            for index, book in enumerate(stack, start=1):  # Enumerate to include indices
                print(f"{index}. {book}")
        else:
            print("Stack is empty!")
    
    elif choice == '5':  # Exit the program
        print("Exiting Book Queue Manager. Goodbye!")
        break
    
    else:
        print("Invalid choice! Please enter a number between 1 and 5.")
