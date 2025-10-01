# register.py

# Step 1: Create an empty list to store student names
students = []  # This list will hold the names of the students entered by the user

# Step 2: Prompt the user to enter 5 students' names and add them to the list
for i in range(5):  # Loop runs 5 times to collect 5 names
    name = input("Enter the name of student " + str(i + 1) + ": ")  # Prompt user for each name
    students.append(name)  # Add each entered name to the students list

# Step 3: Define a function to print the list in reverse order
def print_reverse(names_list):
    """
    This function takes a list of names and prints them in reverse order.
    """
    
    for name in reversed(names_list):  # reversed() function iterates through list in reverse
        print(name)  # Print each name in the reversed order

# Call the function with the students list
print_reverse(students)  # This line triggers the function to print names in reverse order

                 