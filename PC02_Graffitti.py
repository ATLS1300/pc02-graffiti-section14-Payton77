#!/usr/bin/env python
# coding: utf-8

'''
Turtle starter code
ATLS 1300
Author: Dr. Z
Author: PAYTON O'BRIEN
September 3, 2021
'''

import turtle #import the library of commands that you'd like to use

turtle.colormode(255)

# Create a panel to draw on. 
panel = turtle.Screen()
w = 750 # width of panel
h = 750 # height of panel
panel.setup(width=w, height=h) #600 x 600 is a decent size to work on. 
#You can experiment by making it the size of your screen or super tiny!

# Create a colorful background and add Bezos image to it
image = "Bezos.gif"
panel.bgcolor("lightsteelblue1")
panel.bgpic(image)

#=======Add your code here======
turtle.pensize(16)
turtle.color("DarkGreen")
turtle.forward(100)
turtle.right(90)
turtle.forward(100)
turtle.begin_fill()
turtle.right(90)
turtle.forward(100)
turtle.right(90)
turtle.forward(100)
turtle.end_fill()

turtle.up()
turtle.forward(150)
turtle.forward(60)
turtle.right(90)
turtle.forward(120)
turtle.forward(50)
turtle.down()
turtle.pensize(30)
turtle.color("blue")
turtle.pencolor("blue")
turtle.fillcolor("orange")
turtle.begin_fill()
turtle.circle(60)
turtle.end_fill()

turtle.right(90)
turtle.up()
turtle.forward(200)
turtle.forward(300)
turtle.left(90)
turtle.down()
turtle.pensize(15)
turtle.left(90)
turtle.up()
turtle.forward(100)
turtle.right(90)
turtle.down()
turtle.right(45)
turtle.forward(60)
turtle.left(90)
turtle.forward(60)
turtle.left(90)
turtle.forward(60)
turtle.right(45)
turtle.forward(50)
turtle.left(90)
turtle.forward(60)
turtle.right(270)
turtle.forward(60)
turtle.left(45)
turtle.forward(30)
turtle.right(90)
turtle.forward(11)

turtle.up()
turtle.forward(89)
turtle.down()
turtle.color("aquamarine")
turtle.forward(65)



#=======Clean up code (do not change)======
# this code ensures that your script runs correctly each time.
#turtle.done()
