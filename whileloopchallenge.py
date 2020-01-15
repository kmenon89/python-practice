#get the line length ,angle,pen color from user and keep drawing until they give length as 0
#import turtle to draw
import turtle
# declare variables
len=1
angle=0
pcolour="black"

#use while loop
while len != 0 :
    #get input from user about length angle and pen colour
    len=int(input("welcome to sketch /n please enter the length of the line you want to sketch:"))
    angle=int(input("please give the angle of the line to be drawn:"))
    pcolour=input("please eneter the color of pen you want to use:")
    turtle.color(pcolour)
    turtle.right(angle)
    turtle.forward(len)
    
    