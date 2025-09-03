f = open("addr.txt")
z = open("pcodes.txt")


firstline = f.readline()
secondline = z.readline()

address = {}

while firstline != "":
    name = firstline[ :-1].split(sep=":")[0]
    postcode = firstline[ :-1].split(sep=",")[2]
    address[name] = postcode

    firstline = f.readline()

while secondline != "":
    postalcode = secondline[ : -1]
    for name in address:
        if address[name] == postalcode:
           print(name, ":", postalcode)
           secondline = z.readline()
    secondline = z.readline()








