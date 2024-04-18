import turtle

# Create a turtle object
t = turtle.Turtle()

# Function to draw a square


def draw_square():
    for _ in range(4):
        t.forward(100)
        t.right(90)

# Function to draw a triangle


def draw_triangle():
    for _ in range(3):
        t.forward(100)
        t.right(120)

# Function to draw a circle


def draw_circle():
    t.circle(50)


# Move turtle to starting position for square
t.penup()
t.goto(-150, 0)
t.pendown()

# Draw square
draw_square()

# Move turtle to starting position for triangle
t.penup()
t.goto(0, 0)
t.pendown()

# Draw triangle
draw_triangle()

# Move turtle to starting position for circle
t.penup()
t.goto(150, 0)
t.pendown()

# Draw circle
draw_circle()

# Hide the turtle
t.hideturtle()

# Keep the window open
turtle.done()
