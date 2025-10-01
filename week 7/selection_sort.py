import time  # Import the time module to measure execution time

# Step 1: Set up user input
# Create an empty list to store names
names = []

# Inform the user about the input process
print("Enter names one by one. Enter '0' to finish.")

# Use a while loop to collect names until the user enters '0'
while True:
    name = input("Enter a name: ")  # Prompt for a name
    if name == "0":  # Check if the user wants to stop
        break
    names.append(name)  # Add the entered name to the list

# Step 2: Define the bubble sort algorithm
def bubble_sort(input_list):
    sorted_list = input_list.copy()  # Make a copy of the input list
    n = len(sorted_list)  # Get the number of elements in the list
    
    # Outer loop to go through all elements
    for i in range(n):
        # Inner loop for comparing adjacent elements
        for j in range(0, n - i - 1):
            if sorted_list[j] > sorted_list[j + 1]:  # Compare adjacent elements
                # Swap the elements if they are in the wrong order
                sorted_list[j], sorted_list[j + 1] = sorted_list[j + 1], sorted_list[j]
    return sorted_list  # Return the sorted list

# Step 3: Define the selection sort algorithm
def selection_sort(input_list):
    sorted_list = input_list.copy()  # Make a copy of the input list
    n = len(sorted_list)  # Get the number of elements in the list
    
    # Outer loop to go through each element in the list
    for i in range(n):
        min_index = i  # Assume the current element is the smallest
        
        # Inner loop to find the actual smallest element in the remaining unsorted portion
        for j in range(i + 1, n):
            if sorted_list[j] < sorted_list[min_index]:
                min_index = j  # Update the index of the smallest element
        
        # Swap the smallest element with the first element in the unsorted portion
        sorted_list[i], sorted_list[min_index] = sorted_list[min_index], sorted_list[i]
    return sorted_list  # Return the sorted list

# Step 6: Define the time complexity calculator
def time_complexity_calculator(sort_function, dataset):
    start_time = time.time()  # Record the start time
    sort_function(dataset)  # Call the sorting function with the dataset
    end_time = time.time()  # Record the end time
    return end_time - start_time  # Calculate and return the time taken

# Step 7: Measure and compare the time for each algorithm
if names:  # Ensure the names list is not empty
    repetitions = 3  # Number of times to repeat for averaging
    bubble_sort_times = []  # Store times for bubble sort
    selection_sort_times = []  # Store times for selection sort

    for _ in range(repetitions):
        bubble_sort_times.append(time_complexity_calculator(bubble_sort, names))
        selection_sort_times.append(time_complexity_calculator(selection_sort, names))

    # Calculate the average time for each algorithm
    avg_bubble_time = sum(bubble_sort_times) / repetitions
    avg_selection_time = sum(selection_sort_times) / repetitions

    # Output the results
    print(f"\nAverage time for Bubble Sort: {avg_bubble_time:.6f} seconds")
    print(f"Average time for Selection Sort: {avg_selection_time:.6f} seconds")

    # Determine and display the faster algorithm
    if avg_bubble_time < avg_selection_time:
        print("Bubble Sort is faster.")
    elif avg_selection_time < avg_bubble_time:
        print("Selection Sort is faster.")
    else:
        print("Both algorithms have the same average time.")

# Step 4: Call the selection sort function
sorted_names = selection_sort(names)

# Step 5: Print the original and sorted lists
print("\nOriginal list of names:")
print(names)  # Display the original list entered by the user

print("\nSorted list of names using Selection Sort:")
print(sorted_names)  # Display the sorted list

# Step 6: Find the index of the user's name in the sorted list
if names:  # Check if the list is not empty
    user_name = names[0]  # Get the first name entered
    sorted_index = sorted_names.index(user_name)  # Find the index of the name in the sorted list
    print(f"\nYour name '{user_name}' is at index {sorted_index} in the sorted list.")
