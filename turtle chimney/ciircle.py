import turtle as t
import random
#x = random.randint(0,5)
#coord = input('select a circle: ')
#coord.split(sep=',')
#print(coord[0])
for row in range(5):
    for col in range(5):
          t.begin_fill()
          #x = random.randint(0, 5)




          t.color("grey")

          t.circle(10)
          t.penup()
          t.forward(20)
          t.pendown()
          t.end_fill()

    t.penup()
    t.backward(100)
    t.right(90)
    t.forward(20)
    t.left(90)
    t.pendown()
    t.speed(0)


t.exitonclick()






