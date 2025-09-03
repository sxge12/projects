import turtle
turtle.bgcolor('black')
t = turtle.Turtle()
colors = ['red','dark red']
for number in range(800):
    t.forward(number+1)
    t.right(95)
    t.pencolor(colors[number%2])
turtle.done()

