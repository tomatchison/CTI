# Write a program using turtle to draw a triangle and a square with a for loop 
# 25 Oct 2018
# CTI-110 P4T1a: Shapes 
# Tom Atchison
 
# Draw a square and a triangle using turtle.
# Use a while loop or a for loop.

# Start turtle.
import turtle
# See turtle on screen.
wn=turtle.Screen()
# Give turtle optional name.
sid=turtle.Turtle()
# Give turtle turtle shape and wish ("waifu") was option.
sid.shape ("turtle")
# Use for loop for the square.
for a in range (4):
   sid.forward (125)   
   sid.left (90)
# Use for loop for the triangle.
for b in range (3):
   sid.left (120)
   sid.forward (125)
# Exit turtle.
turtle.exitonclick()


