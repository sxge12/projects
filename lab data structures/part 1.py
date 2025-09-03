myDict = {"chocolates":5, "ice cream":5, "cocktail": 5}
product = input("what would you like to order?")
while product != " ":
   quantity = int(input("items number?"))
   if product == "chocolates":
    price = 1.5
   elif product == "ice cream":
    price = 2
   else:
    price = 7


   if quantity <= myDict[product]:
    print ("total price:", quantity*int(price))
    myDict[product] = myDict[product] - quantity
   else:
    print ("we our out of stock!")
    product = input("what would you like to order")