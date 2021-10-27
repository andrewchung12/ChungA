#   a117_traversing_turtles.py
#   Add code to make turtles move in a circle and change colors.
import turtle as trtl

# create an empty list of turtles
my_turtles = []

# use interesting shapes and colors
turtle_shapes = ["arrow", "turtle", "circle", "square", "triangle", "classic"]
turtle_colors = ["red", "blue", "green", "orange", "purple", "gold"]

for s in turtle_shapes:
  t = trtl.Turtle(shape=s)
  my_turtles.append(t)
  new_color=turtle_colors.pop()
  t.pencolor(new_color)
  t.fillcolor(new_color)
  t.penup()

# defines what startx is 
start_x = 0
start_y = 0
direction = 90
#makes turtle start(0,0) and also moves it upafter running 
for t in my_turtles:
  t.goto(start_x, start_y)
  t.setheading(direction)
  t.pendown()
  t.right(45)     
  t.forward(50)
  

#adds 50 to the value of startx
  start_x = t.xcor()
  start_y = t.ycor()
  direction=t.heading()
  

wn = trtl.Screen()
wn.mainloop()