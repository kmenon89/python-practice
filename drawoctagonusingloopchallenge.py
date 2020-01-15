#draw any shape using input from user about the shape
#draw inner shapes with the same input

import turtle


#get input from user about number of sides
sides=int(input("please enter the number of sides of the figure:"))

#declare the variable
len=100

print(sides)
for step in range(sides):
    turtle.forward(len)
    turtle.right(360/sides)
    for step in range(0,sides,1):
        turtle.forward(len/2)
        turtle.right(360/sides)