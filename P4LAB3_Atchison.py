# Create my initials using turtle 
# 25 Oct 2018
# CTI-110 P4T1b: Initials 
# Tom Atchison



# Start turtle.
import turtle
import random
# See turtle on screen.
wn=turtle.Screen()
wn.bgcolor("green")
# Give turtle optional name.
sid=turtle.Turtle()
sid.speed(20)
# Give turtle shape.
sid.shape ("turtle")


# create a list of colours
sfcolor = ["brown", "red", "orange", "yellow", "magenta"]

# create a function to create different size leaves
def leaf(size):
# move the pen into starting position
    sid.penup()
    sid.forward(10*size)
    sid.left(45)
    sid.pendown()
    sid.color(random.choice(sfcolor))
    # draw a leaf
    for i in range(8):
        branch(size)   
        sid.left(45)
    

