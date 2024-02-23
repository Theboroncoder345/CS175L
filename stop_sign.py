import math
import turtle
# Arnav Vasa
# CS175L
# Stop Sign
# Named constants
WINDOW_WIDTH = 400
WINDOW_HEIGHT = 400
ANIMATION_SPEED = 0
NUM_SIDES = 8
LENGTH = 100
ANGLE = 45
TEXT_X = -5
TEXT_Y = -10

# Size the window.
turtle.setup(WINDOW_WIDTH, WINDOW_HEIGHT)

# Calculate the diameter of the octagon so we
# can center it in the graphics window.
#                s
#        ---------------
#       / |             \
#  s   /  |              \
#     /   | x             \  s
#    /    |                \
#   |------                 |
#   |   x                   |
#   |                       |
#   To get the diameter:
#     diameter = s + 2 * x
#   We know that s is 100.
#   Use Pythagoras to get x:
#   s^2 = x^2 + x^2
#   s^2 = 2*x^2
#   x = s / sqrt(2)
s = LENGTH
x = s / math.sqrt(2)
diameter = s + (2 * x)
# Initialize the turtle.
turtle.speed(ANIMATION_SPEED)

# Move the turtle to the starting point.
turtle.penup()
turtle.goto((-57,150))
turtle.pendown()

# Draw the octagon.
turtle.color('Red')
turtle.begin_fill()
for i in range(NUM_SIDES):
    turtle.fd(LENGTH)
    turtle.right(ANGLE)
turtle.end_fill()
turtle.color('White')
turtle.width(40)
for i in range(NUM_SIDES):
    turtle.fd(LENGTH)
    turtle.right(ANGLE)
turtle.color('Red')
turtle.width(10)
for i in range(NUM_SIDES):
    turtle.fd(LENGTH)
    turtle.right(ANGLE)
# Display 'STOP'
turtle.color('White')
turtle.penup()
turtle.goto((TEXT_X,TEXT_Y))
turtle.pendown()
turtle.write("STOP", False, align="Center", font=('Arial', 48, 'bold'))
