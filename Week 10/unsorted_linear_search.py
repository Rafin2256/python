# Unsorted Linear Search Implementation

def linear_unsorted(ListData, value):
    index = 0
    # Fixed the loop condition to ensure it stops when the index is out of range or the value is found
    while index < len(ListData) and ListData[index] != value:
        index += 1  # Fixed the increment to increase index correctly
    
    # Fixed the condition to return -1 if the value is not found
    if index >= len(ListData):
        return -1
    else:
        return index

# Corrected function name in the print statement and removed quotes around the number
original_array = [100, 24, 1, 69, 32]

# Fixed function name in the print statement from linear_sorted to linear_unsorted
print("Search number 42:", linear_unsorted(original_array, 42))
print("Search number 69:", linear_unsorted(original_array, 69))
