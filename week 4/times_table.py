#program to generate multiplication of table 

#Ask the user for the number they want the multiplication for

number =int(input("Enter a whole number: "))

#use a for loop to iterate through numbers 1 to 10

for i in range(1, 11):
    print(f"{i}*{number} = {i * number}")#f before the
    #string is formated string is like fill in the blank
    #first part before this = is getting the number and after is like
    #showing the result
