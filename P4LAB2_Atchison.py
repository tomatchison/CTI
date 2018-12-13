# Create my initials using turtle 
# 25 Oct 2018
# CTI-110 P4T1b: Initials 
# Tom Atchison


# Create initials using turtle.
# Change color of turtle.
# Change size of line.
# Start turtle.
import turtle
# See turtle on screen.
wn=turtle.Screen()
wn.bgcolor("yellow")
# Give turtle optional name.
sid=turtle.Turtle()
# Give turtle shape.
sid.shape ("turtle")
# Change line color.
sid.color("red")
# Change line size.
sid.pensize(4)
# Move sid to start position.
sid.left(90)
sid.penup()
sid.forward(250)
sid.left(90)
sid.forward(250)
sid.left(180)
# Instruct sid when and where to write.
# Create bar for letter T.
sid.pendown()
sid.forward(200)
sid.penup()
# Create leg for letter T
sid.right(180)
sid.forward(100)
sid.left(90)
sid.pendown()
sid.forward(250)
sid.penup()
# Move to starting area for letter A.
sid.left(90)
sid.forward(75)
# Create left and right legs for letter A.
sid.left(75)
sid.pendown()
sid.forward(250)
sid.right(150)
sid.forward(250)
# Move to position to create bar for letter A.
sid.penup()
sid.left(165)
sid.forward(125)
# Create bar for the letter A
sid.left(90)
sid.pendown()
sid.forward(125)
# Good job sid, take a break.
sid.penup()
for a in [0,1,2,]:
    sid.forward(200)
    sid.left(90)
# Exit turtle.
turtle.exitonclick()
