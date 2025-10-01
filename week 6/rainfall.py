# Function to display the histogram with vertical bars
def display_histogram(rainfall_data):
    # Find the maximum rainfall value to set the histogram's height
    max_rainfall = max(rainfall_data.values())
    
    # Print the header for the histogram
    print("Rainfall Histogram")
    print("------------------")
    
    # Generate histogram bars, with each '*' representing 10mm of rain
    # Loop from max_rainfall down to 10, decreasing by 10 each time
    for level in range(max_rainfall, 0, -10):
        # Print each month with '*' symbols corresponding to the rainfall level
        row = ''
        for month, rainfall in rainfall_data.items():
            if rainfall >= level:
                row += " *  "
            else:
                row += "    "  # Spaces for alignment if rainfall < current level
        print(row)  # Print each row level of the histogram
    
    # Print month labels at the bottom of the histogram
    print("\n" + "  ".join(rainfall_data.keys()))

# Main program
def main():
    # Setup rainfall data for each month
    rainfall_data = {
        'Jan': 23, 'Feb': 45, 'Mar': 12, 'Apr': 10, 'May': 33,
        'Jun': 90, 'Jul': 94, 'Aug': 76, 'Sep': 10, 'Oct': 15, 
        'Nov': 120, 'Dec': 22
    }
    
    # Call the function to display the histogram
    display_histogram(rainfall_data)

# Start the program
main()
