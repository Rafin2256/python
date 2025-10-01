import turtle
wn = turtle.Screen()  #creating screen
wn.title("Traffic Light Simulation") #creating title
wn.bgcolor("darkgrey") #creating color

light = turtle.Turtle() #creating an object name light to represent traffic light
light.shape("circle") #creating shape of the turtle light
light.shapesize(3) #increasing the spape size 
light.penup() #lifts the pen sp the turtle doesnt draw when it moves
light.goto(0,0) #POSITION OF THE LIGHT AT THE CENTER OF THE SCREEN

def update_light_color(color):  #a function that takes color argument 
    light.fillcolor(color) #fill color to simulate traffic lights
def go_green():
    update_light_color("green")

def slow_down():
    update_light_color("yellow")

def stop():
    update_light_color("red")

wn.onkey(go_green, "g")  #links a keypress to a specific funtion
wn.onkey(slow_down, "y")
wn.onkey(stop, "r")
wn.listen() #start listening keyboard command .
wn.mainloop() #keeping the turtle creen open
