#   a116_buggy_image.py
import turtle as trtl
# instead of a descriptive name of the turtle such as painter,
# a less useful variable name spider is used
spider = trtl.Turtle()
spider.pensize(40)
spider.circle(20)
#how many legs spider will have
legs = 8
#length of spider legs
length_of_legs = 100
#determines where the angle of each spider leg
angle_of_legs = 380 / legs
print("z=", angle_of_legs)
spider.pensize(5)
incrementing_counter = 0
#draw legs
while (incrementing_counter < legs):
  print("z*n=", angle_of_legs*incrementing_counter)
  spider.goto(0,0)
  spider.setheading(angle_of_legs*incrementing_counter)
  spider.forward(length_of_legs)
  spider.forward(length_of_legs)
  incrementing_counter = incrementing_counter + 1
spider.hideturtle()
wn = trtl.Screen()
wn.mainloop()