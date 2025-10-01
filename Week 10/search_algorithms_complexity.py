from timeit import repeat  # Import repeat to measure execution time of code
from random import randint  # Import randint to generate random numbers

# Function to perform unsorted linear search
def linear_unsorted(ListData, value):
    """
    Searches for a value in an unsorted list by checking each item one by one.
    :param ListData: The list to search in.
    :param value: The value to search for.
    :return: The index of the value if found, otherwise -1.
    """
    for i, item in enumerate(ListData):
        if item == value:  # If the item matches the value, return the index
            return i
    return -1  # Return -1 if the value is not found

# Function to perform sorted linear search
def linear_sorted(ListData, value):
    """
    Searches for a value in a sorted list. Stops searching if the current item is greater than the value.
    :param ListData: The sorted list to search in.
    :param value: The value to search for.
    :return: The index of the value if found, otherwise -1.
    """
    for i, item in enumerate(ListData):
        if item == value:  # If the item matches the value, return the index
            return i
        elif item > value:  # Stop searching if the current item is greater than the value
            break
    return -1  # Return -1 if the value is not found

# Function to perform binary search
def binary_search(ListData, value):
    """
    Searches for a value in a sorted list by repeatedly dividing the search space in half.
    :param ListData: The sorted list to search in.
    :param value: The value to search for.
    :return: The index of the value if found, otherwise -1.
    """
    low, high = 0, len(ListData) - 1  # Set the initial range for searching
    while low <= high:  # Continue as long as the range is valid
        mid = (low + high) // 2  # Find the middle index
        if ListData[mid] == value:  # If the middle item matches, return the index
            return mid
        elif ListData[mid] < value:  # If the value is larger, search in the right half
            low = mid + 1
        else:  # If the value is smaller, search in the left half
            high = mid - 1
    return -1  # Return -1 if the value is not found

# Function to measure the time complexity of each search method
def measure_time_complexity(unsorted_array, sorted_array, value):
    """
    Measures the execution time for each search method and determines the fastest one.
    :param unsorted_array: The unsorted list to search in.
    :param sorted_array: The sorted list to search in.
    :param value: The value to search for.
    """
    # Setup code for timeit
    setup_code_unsorted = "from __main__ import linear_unsorted, unsorted_array, value"
    setup_code_sorted = "from __main__ import linear_sorted, sorted_array, value"
    setup_code_binary_sorted = "from __main__ import binary_search, sorted_array, value"

    # Statements to execute
    linearUnsortedStmt = "linear_unsorted(unsorted_array, value)"
    linearSortedStmt = "linear_sorted(sorted_array, value)"
    binarySortedStmt = "binary_search(sorted_array, value)"

    # Measure time for unsorted linear search
    linear_unsorted_min = min(repeat(stmt=linearUnsortedStmt, setup=setup_code_unsorted, repeat=3, number=1000))
    print(f"Linear Search (Unsorted) - Execution time: {linear_unsorted_min:.6f} seconds")

    # Measure time for sorted linear search
    linear_sorted_min = min(repeat(stmt=linearSortedStmt, setup=setup_code_sorted, repeat=3, number=1000))
    print(f"Linear Search (Sorted) - Execution time: {linear_sorted_min:.6f} seconds")

    # Measure time for binary search
    binary_sorted_min = min(repeat(stmt=binarySortedStmt, setup=setup_code_binary_sorted, repeat=3, number=1000))
    print(f"Binary Search (Sorted) - Execution time: {binary_sorted_min:.6f} seconds")

    # Determine the fastest search method
    data = {
        "Linear Search (Unsorted)": linear_unsorted_min,
        "Linear Search (Sorted)": linear_sorted_min,
        "Binary Search (Sorted)": binary_sorted_min
    }
    print(f"The search with the shortest time complexity is: {min(data, key=data.get)}")

# Define the size of the list and generate random data
ARRAY_SIZE = 30  # You can change this size as needed
unsorted_array = [randint(0, ARRAY_SIZE * 10) for _ in range(ARRAY_SIZE)]  # Create an unsorted list
sorted_array = sorted(unsorted_array)  # Create a sorted version of the list
value = 5  # The value to search for (you can change this)

# Print the arrays and the value to be searched
print("Value to be searched:", value)
print("Unsorted Array:", unsorted_array)
print("Sorted Array:", sorted_array)

# Call the function to measure time complexity
measure_time_complexity(unsorted_array, sorted_array, value)
