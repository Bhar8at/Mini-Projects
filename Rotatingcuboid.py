# Rotating cuboid
# import turtle package
import turtle
from math import *
import time

# important variables
e = {}
a = 100  # amplitude of oscillation
T = 2  # Time interval of oscillation
o = (2*pi)/T  # Angular frequency
t = 1  # time taken
c = {1:0, 2:0}
# function for movement of an object
def moving_object(move):
  global t1, t2, e
  # to fill the color in ball
  move.fillcolor('orange')

  # start color filling
  move.begin_fill()
  if move == t1:
       e = {} # end points of the square
  # draw circle
  # move.circle(20)
  for i in range(4):
      if move == t1:
          print("satisfied")
          e[i] = t1.pos()
          print(e)
          move.fd(50)
          move.rt(90)
      if move == t2:
          t2.color("white")
          t2.pendown()
          prev = t2.pos()
          t2.goto(e[i])
          t2.goto(prev)
          t2.color('white')
          move.fillcolor('orange')
          move.fd(50)
          move.rt(90)


  # end color filling
  move.end_fill()


# Driver Code
if __name__ == "__main__":

  # create a screen object
  screen = turtle.Screen()

  # creating turtles
  t1 = turtle.Turtle()
  t1.rt(15)
  t2 = turtle.Turtle()
  t2.rt(15)

  # set screen size
  screen.setup(400, 600)

  # screen background color
  screen.bgcolor('black')

  # screen updaion
  screen.tracer(0)


  # set a turtle object color
  t1.color('white')
  t2.color('white')
  # set turtle object speed
  t1.speed(0)
  t2.speed(0)
  # set turtle object width
  t1.width(2)
  t2.width(2)

  # hide turtle object
  t1.hideturtle()
  t2.hideturtle()

  # turtle object in air
  t1.penup()
  t2.penup()

  # set initial position
  t1.goto(0, 0)
  t2.goto((0,0))

  # move turtle object to surface
  t1.pendown()
  t2.pendown()

  # infinite loop
  while True:

      # clear turtle work
      t1.clear()
      t2.clear()
      x = a * sin(o * t)
      x1 = a*sin(o*t + pi)
      y = a * sin(o*t + (pi/2))
      y1 = a*sin(o*t +(pi/2))
      print(x)
      t += 0.007
      time.sleep(0.0000000000001)
      t1.goto(x, y)
      t2.goto(x1, y1)
      # call function to draw ball
      moving_object(t1)
      moving_object(t2)
      print(e)
      # update screen
      screen.update()