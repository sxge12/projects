
#import turtle
#for i in range(6):
 #turtle.forward(100)
 #turtle.right(60)

import turtle


for row in range(8):
      for col in range(8):
         if (row + col) % 2 == 0:
           turtle.color("yellow")
         else:
           turtle.color("green")
         turtle.begin_fill()
         for f in range(4):
            turtle.forward(20)
            turtle.right(90)
         turtle.end_fill()

         turtle.penup()
         turtle.forward(20)
         turtle.pendown()

      turtle.penup()
      turtle.backward(160)
      turtle.right(90)
      turtle.forward(20)
      turtle.left(90)
      turtle.pendown()
turtle.exitonclick()












