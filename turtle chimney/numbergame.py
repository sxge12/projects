#We are going to write a simple text-based interactive game, that:
#(1) selects a random integer between 1 and 100 inclusive
#(2) repeatedly asks the user to type in a guess for the number, until their guess is correct
#(3) stops when the user is correct and reports the number of guesses the user had
#Can you see how each of these steps might map onto Python constructs we have already
#encountered?
#(1) We know how to generate a random integer in a certain range of values, using
#random.randint
#(2) This repeated execution, with a condition, looks like a while loop. A user guess can be read
#in as a string with the input function, and then converted to an integer with the int function.
#We can add one to a count of the number of guesses each time we execute the loop.
#(3) at the end, we print a congratulations message and report the number of guesses
import random
numba = random.randint(1, 101)
print(numba)
#numberguess = int(input("Guess the number: "))
guesscounter = 0

while True:
  numberguess = int(input("Guess the number: "))

  if numberguess != numba:
    guesscounter += 1
    print(numberguess)
  else:
    print('you got it!')
    print(f'it took you: {guesscounter} tries.')
    break

#couldve probably done the if/else statement in reverse and it might of worked but oh well