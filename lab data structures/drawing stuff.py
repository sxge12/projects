import turtle


f = open("drawing.txt")

drawing = []
z = 0
nextLine = f.readline()
while nextLine != "":
    bits = nextLine[: - 1].split(",")

    nextPart = {"x": int(bits[0]), "y": int(bits[1]), "direction": int(bits[2]), "len": int(bits[3])}
    drawing.append(nextPart)

    nextLine = f.readline()

nextInput = input("Enter (d)raw, (l)ist lines, (c)hange a line, (q)uit: ")

while nextInput != "q":
    if nextInput == "d":
        for line in drawing:
            turtle.penup()
            turtle.goto(line["x"], line["y"])
            turtle.pendown()
            turtle.setheading(line["direction"])
            turtle.forward(line["len"])
        turtle.exitonclick()
    elif nextInput == "l":
        for line in drawing:
            z += 1
            print( drawing[z] +  "({0},{1}), direction {2}, length {3}".format(line["x"], line["y"], line["direction"], line["len"]))
    elif nextInput == "c":
        lineNum = int(input("Which line? start from zero"))
        newLine = input("Type in the four numbers for the changed line, separated by spaces")
        bits = newLine.split()
        newPart = {"x": int(bits[0]), "y": int(bits[1]), "direction": int(bits[2]), "len": int(bits[3])}
        drawing[lineNum] = newPart
    else:
        print("input not understood")
    nextInput = input("What now? ")