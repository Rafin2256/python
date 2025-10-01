# Step 1: Create a new Python file called bubble_sort.py and save it in your week 8 folder.

# Step 2: Set up the user input
# Create an empty list called names
names = []

# Create a while loop that runs until the user enters 0 to finish inputting names
print("Enter names one by one. Enter '0' to finish.")
while True:
    name = input("Enter a name: ")
    if name == "0":
        break
    names.append(name)

# Step 3: Create the bubble sort algorithm using the example in the lecture
# Define the bubble sort function
def bubble_sort(input_list):
    sorted_list = input_list.copy()  # Make a copy of the input list
    n = len(sorted_list)
    for i in range(n):
        for j in range(0, n - i - 1):
            if sorted_list[j] > sorted_list[j + 1]:
                # Swap if the element found is greater than the next element
                sorted_list[j], sorted_list[j + 1] = sorted_list[j + 1], sorted_list[j]
    return sorted_list

# Step 4: Call your bubble sort function
# Make a call to the bubble sort function and pass it a copy of the list of names
sorted_names = bubble_sort(names)

# Step 5: Print the lists
print("\nOriginal list of names:")
print(names)
print("\nSorted list of names:")
print(sorted_names)

# Step 6: Run your program and check the index of your name
# Assuming the user enters their own name first, find the index of the first entered name in the sorted list
if names:
    user_name = names[0]
    sorted_index = sorted_names.index(user_name)
    print(f"\nYour name '{user_name}' is at index {sorted_index} in the sorted list.")
