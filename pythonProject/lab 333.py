import turtle
file = open ("surpise.txt")
firstline = file.readline() # reads the first line
colours = firstline.split(',') # creates a list of colours found in the first line of the file
for i in range (8):
    radius = int(file.readline())
    print(radius)# reads the numbers representing the radius of the semi-circles
    turtle.color(colours[i]) #sets the colour of each semi-circle
    turtle.left(90)
    turtle.begin_fill()
    turtle.circle(radius, 180)
    turtle.left(90)
    turtle.forward(2*radius)
    turtle.end_fill()
    turtle.back(10)
turtle.exitonclick() 