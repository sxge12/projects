import math
import turtle
def house(sidelength):
    rooflength = math.sqrt( 2 ) * sidelength/2
    turtle.begin_fill()
    turtle.forward( sidelength )
    turtle.left( 90 )
    turtle.forward( sidelength )
    turtle.left( 45 )
    turtle.forward( rooflength )
    turtle.left( 90 )
    turtle.forward( rooflength )
    turtle.left( 45 )
    turtle.forward( 100 )
    turtle.left( 90 )
    turtle.end_fill()
    turtle.exitonclick()

def rown(n, size):
    for row in range(n):


            # rooflength = math.sqrt(2) * size / 2
            # turtle.begin_fill()
            # turtle.forward(size)
            # turtle.left(90)
            # turtle.forward(size)
            # turtle.left(45)
            # turtle.forward(rooflength)
            # turtle.left(90)
            # turtle.forward(rooflength)
            # turtle.left(45)
            # turtle.forward(100)
            # turtle.left(90)
            #
            #
            # turtle.penup()
            # turtle.forward(size)
            # turtle.pendown()
            #
            # turtle.end_fill()




rown(3,100)


