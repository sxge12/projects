#f = open("partc.txt")
#s = f.readline()
#counter = 0


userinput = int(input("what is your number?: "))
countertotal = 1

while userinput <= 100:
    nxtnumber = input("next number?: ")
    userinput = userinput + int(nxtnumber)
    countertotal = countertotal + 1
print('the sum of these numbers is ', userinput)
print('this includes ', countertotal , ' numbers')









































#s = open("readings.txt")
#f = s.readline()
#while f != "":
   # number = int(f)
  #  if number < 0:
   #     number = 0
    #print(number)
   # f = s.readline()
#counter = 0
#while f != "":
    #daystemp = int(f)
    #if daystemp > 0:
        #dayscounter = counter + 1
    #f = s.readline()
#print(dayscounter)



