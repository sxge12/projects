output = {}

f = open("chat.txt")
z = f.readline()

while z !=" ":
 z = f.readline()
 s = z.split(sep=" ")
 name = " ".join(s[2:4])
 if name != s[2]:
     output["identification"] = name

print(output)





