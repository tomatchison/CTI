# Draw something using a nested loop in a turtle program.
# 26 October 2018
# CTI-110 P4LAB-Nested Loops.py
# Tom Atchison


# Start turtle.
import turtle
# See turtle on screen.
wn=turtle.Screen()
# Give turtle optional name.
sid=turtle.Turtle()
# Give turtle turtle shape.
sid.shape ("turtle")
# Choose pensize
sid.pensize(3)
# Choose colors
colors=["red","green","orange","blue"]
# Change sid's colors 
for x in range(4):
    sid.color(colors[x%4])
    sid.left(90)
# and draw shapes using nested loop.
    for a in range (7):
        sid.forward (30)   
        sid.left (45)
# End program. 
sid.write("The End",move=True,align="center",font=("Freestyle Script",50, \
            "normal"))
sid.penup
sid.right (180)
# Exit turtle
turtle.exitonclick()

