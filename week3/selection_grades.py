
#university grade calculator 

#geting user input 
grade = float(input("Enter your grade percentage: "))

#computing the data
if grade < 50:
    print("failed")
elif grade < 60:
    print("pass")
elif grade < 70:
    print("merit")
else :
    print("distinction")