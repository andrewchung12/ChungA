#   a113_flower.py
#   This code draws a flower.
import turtle as trtl

painter = trtl.Turtle()
painter.speed(10)

# stem
painter.color("green")
painter.pensize(15)
painter.goto(0, -150)
painter.setheading(90)
painter.forward(100)
#  leaf
painter.setheading(270)
painter.circle(20, 120, 20)
painter.setheading(90)
painter.goto(0, -60)
# rest of stem
painter.forward(60)
painter.setheading(0)

# change pen
painter.penup()
painter.shape("circle")
painter.turtlesize(2)

# draw flower
painter.color("darkorchid")
painter.goto(20,180)
petals = 0
while (petals < 13):
  painter.right(50)
  painter.forward(30)
  painter.stamp()
  petals = petals + 1
  
wn = trtl.Screen()
wn.mainloop()