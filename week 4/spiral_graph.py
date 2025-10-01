import turtle  #import necessary modules and set up the screen
import random
#sett up the screen
screen = turtle.Screen()
screen.title("Colorful spiral Activity")
screen.bgcolor("black")
# create and configure the turtle
t = turtle.Turtle()
t.speed(0) # Fastest speed
t.width(2)
#define colors
colors = ["red", "orange", "yellow", "green", "blue", "purple"]

#create a helper function to select color
def random_color():
    return random.choice(colors)
# main drawing loop
length = 5  #initialize lengh variable
 
while length <200:
    t.color(random_color())  # set turtle color to a random color

# use a for loop to draw multiple circles of vaying sizes
    for i in range(1, 11):  # Draw 10 circles for each lenght
        if length % 2 == 0:  #check if the length is even
            t.circle(length/4) #even lenght draw a smaller circle 
        else:
            t.circle(length/2) #odd length draw a smaller cirle

        t.left(10) #rotate the turtle left by 10 degrees
        length += 2 #increase the length by 2 after each circle

        t.left(10)
        length += 5

turtle.done()  #finish the drwaing