import turtle as j
j.speed(0)
def move(xx,yy):
  j.penup()
  j.goto(xx,yy)
  j.pendown()

move(-200,0)
j.forward(400)
move(0,0)
j.left(90)
j.forward(200)
j.backward(400)
move(-200,-200)
for x in range(4):
  j.forward(400)
  j.right(90)
j.pencolor("light grey")
move(-200,0)
j.right(90)
for i in range(39):
  j.forward(10)
  j.left(90)
  j.forward(200)
  j.backward(400)
  j.forward(200)
  j.right(90)
move(200,200)
j.right(90)
for y in range(39):
  forward(1)



wn = j.Screen()
wn.mainloop()