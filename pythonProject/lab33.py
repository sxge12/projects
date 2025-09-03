mylist = [ 3, 7, -1, 2, -10, 6, 8 ]
posinlist = 0

while posinlist < len(mylist)-1:
    posinlist = posinlist + 1
    mylistin = int(mylist[posinlist])
    if mylistin < 0:
        mylistin = 0

    print(mylistin)



