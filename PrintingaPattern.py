import turtle
t=turtle.Turtle()
turtle.bgcolor("black")
t.speed(0)
colors=["yellow","blue","green","orange","purple","red"]
for i in range(200):
    t.pencolor(colors[i%6])
    t.forward(i*2)
    t.right(61)
turtle.done()
