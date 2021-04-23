import turtle
a = turtle.Screen()
tartaruga = turtle.Turtle()
tartaruga.speed(0)

for i in range(30):
    for i in range(4):
      tartaruga.forward(100)
      tartaruga.right(90)
    tartaruga.right(25)

a.exitonclick()