# Step 4: Write the linear sorted search algorithm to return the index of the
# inputted country, if the country doesn't exist return -1

# Read the countries from a file
countries = []
with open('./Week 10/countries.txt', 'r') as file:
    countries = [line.strip() for line in file]

# Step 5: Take user input asking them to enter a country
input_country = input("Enter a country: ")

# Step 6: Call the linear sorted function and pass the countries list and
# inputted country as arguments

def linear_sorted_search(countries, target):
    for i, country in enumerate(countries):
        if country == target:
            return i
    return -1

# • Set the returned value to a variable called index
index = linear_sorted_search(countries, input_country)

# Step 7: Create an if/else statement:
# • If: the returned index is greater or equal to 0, print the index along with a suitable label
if index >= 0:
    print(f"The country '{input_country}' is at index: {index}")
# • Else: print a statement saying the entered country doesn't exist in the list
else:
    print(f"The country '{input_country}' doesn't exist in the list.")
