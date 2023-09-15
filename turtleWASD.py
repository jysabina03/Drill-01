import turtle
import random

def move_W():
    turtle.stamp()
    turtle.setheading(90)
    turtle.forward(50)
    
def move_A():
    turtle.stamp()
    turtle.setheading(180)
    turtle.forward(50)
    
def move_D():
    turtle.stamp()
    turtle.setheading(0)
    turtle.forward(50)
    
def move_S():
    turtle.stamp()
    turtle.setheading(-90)
    turtle.forward(50)
    

turtle.shape("turtle")

turtle.onkey(move_W,'w')
turtle.onkey(move_S,'s')
turtle.onkey(move_D,'d')
turtle.onkey(move_A,'a')
turtle.listen()
