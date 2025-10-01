import turtle
import random

# Setup the screen
screen = turtle.Screen()
screen.title("Random Sprites")
screen.setup(600, 600)
screen.bgcolor("black")
screen.tracer(0)  # Turn off animation updates for smoother movement

# Data structures
sprites = []  # List to store active sprites
color_counts = {  # Dictionary to store counts of each color
    "yellow": 0,
    "red": 0,
    "blue": 0,
    "green": 0,
    "purple": 0,
    "orange": 0,
}

# Counter display turtle
counter = turtle.Turtle()
counter.penup()
counter.hideturtle()
counter.color("white")
counter.goto(-280, 250)

def update_counter():
    """Update the counter display on the screen."""
    counter.clear()
    y = 250  # Start from the top
    for color, count in color_counts.items():
        counter.color(color)  # Set the color for the counter
        counter.goto(-280, y)  # Move to the position
        counter.write(f"{color}: {count}", font=("Arial", 12, "normal"))  # Write text
        y -= 20  # Move down for the next line

def create_sprite():
    """Create a new sprite and add it to the screen."""
    t = turtle.Turtle()
    t.penup()
    t.shape("triangle")  # Set the shape to a triangle
    colors = list(color_counts.keys())  # Get a list of all possible colors
    color = random.choice(colors)  # Pick a random color
    t.color(color)  # Set the turtle's color

    # Set a random x position at the bottom of the screen
    x = random.randint(-250, 250)
    t.goto(x, -250)  # Start at the bottom
    t.setheading(90)  # Point upward

    sprites.append(t)  # Add the sprite to the list
    color_counts[color] += 1  # Increase the count for the color
    update_counter()  # Update the counter display

def move_sprites():
    """Move sprites and manage them."""
    for sprite in sprites[:]:  # Use a copy of the list to modify it safely
        sprite.forward(5)  # Move the sprite upward

        # Remove sprite if it goes off the top of the screen
        if sprite.ycor() > 300:
            color_counts[sprite.pencolor()] -= 1  # Decrease the color count
            update_counter()  # Update the counter display
            sprite.hideturtle()  # Hide the sprite
            sprites.remove(sprite)  # Remove it from the list

    # Randomly create a new sprite (10% chance)
    if random.random() < 0.1:
        create_sprite()

    # Update the screen
    screen.update()

    # Continue movement with a timer
    screen.ontimer(move_sprites, 50)

# Start the animation
move_sprites()

# End program when clicking the screen
screen.exitonclick()
