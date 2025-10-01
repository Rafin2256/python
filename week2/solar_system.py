import turtle

# Initialize the screen
screen = turtle.Screen()
screen.setup(width=800, height=600)  # Set screen size
screen.bgcolor("black")  # Set background color

# Initialize the turtle
t = turtle.Turtle()
t.speed(0)  # Set drawing speed to fastest

# Function to create a planet
def create_planet(color, radius):
    t.color(color)
    t.begin_fill()
    t.circle(radius)
    t.end_fill()

# Function to move the pen down
def move_pen_down(distance):
    t.penup()
    t.right(90)  # Rotate turtle to face downward
    t.forward(distance)  # Move down by specified distance
    t.left(90)  # Rotate turtle back to original position
    t.pendown()

# Create the planets
create_planet("orange", 60)  # Orange planet
move_pen_down(70)

create_planet("gray", 20)  # Gray planet
move_pen_down(100)

create_planet("red", 40)  # Red planet
move_pen_down(100)

create_planet("green", 30)  # Green planet

# Finish drawing
turtle.done()
