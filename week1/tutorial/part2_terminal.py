import turtle  # Import the turtle library

# Create a screen
screen = turtle.Screen()
screen.setup(width=0.5, height=0.75)  # Set the screen size
screen.bgcolor(1, 1, 0)  # Set background color to yellow
screen.title("Turtle Movement Activity")  # Set the title of the window

# Create a turtle object and initialize it as 't'
t = turtle.Turtle()

# Step 1: Move turtle pointer from origin (0, 0) to the 3rd quadrant
t.penup()  # Lift the pen so it doesn't draw a line
t.goto(-100, -100)  # Move to the 3rd quadrant (negative x, negative y)
t.pendown()  # Put the pen down to start drawing

# Step 2: Change pointer color to blue
t.color("blue")

# Step 3: Change the size of the turtle pointer
t.shapesize(2)  # Make the turtle twice as large

# Step 4: Move turtle pointer from the 3rd quadrant to the 1st quadrant
t.goto(100, 100)  # Move to the 1st quadrant (positive x, positive y)

# Keep the window open
screen.mainloop()
