import random

import turtle as t

from random import randint

def armright():
    t.left(180)
    t.penup()
    t.forward(150)
    t.pendown()
    t.right(135)
    t.forward(100)
def armleft():
    t.left(180)
    t.penup()
    t.forward(100)
    t.pendown()
    t.left(90)
    t.forward(100)
def head():
    t.left(180)
    t.forward(100)
    t.right(135)
    t.left(180)
    t.penup()
    t.right(90)
    t.pendown()
    t.circle(40, 360,)
def legs():
    t.right(90)
    t.penup()
    t.forward(150)
    t.pendown()
    t.left(50)
    t.forward(100)
    t.penup()
    t.right(180)
    t.forward(100)
def otherleg():
    t.left(80)
    t.pendown()
    t.forward(100)
def body():
    t.penup()
    t.left(90)
    t.forward(80)
    t.left(90)
    t.pendown()
    t.forward(150)
    t.left(90)
    t.forward(250)
    t.left(90)
    t.forward(50)
    t.right(180)
    t.forward(100)
    t.penup()
    t.left(180)
    t.forward(50)
    t.left(90)
    t.forward(250)
    t.right(90)
    t.forward(150)
    t.right(90)
    t.penup()
    t.forward(80)
    t.pendown()
    t.forward(150)

def hangmangame():
    print("welcome to hangman")
    f = open("hangmanwords.txt")
    readfile = f.readlines()
    wordkey = 1
    #letters = []
    words = {}
    userprompt = input("would you like to play: (y)es or (n)o: ")
    for line in readfile:
        word = line.strip()
        words[wordkey] = word
        wordkey += 1
    randomword = randint(0, len(words) - 1)

    if userprompt == "y":
        word = words[randomword]
        wrd_underscores = ["_"]*len(word)
        print("your word is: ", " " .join(wrd_underscores), "long")

        max_guesses = 6
        guessedletters = []

        while max_guesses > 0 and "_" in wrd_underscores:
            userguess = input("guess a letter: ")

            if userguess in guessedletters:
                print("you've already guessed this letter guess another")
            guessedletters.append(userguess)

            if userguess in word:
                print("one letter down good job!")
                for i in range(len(word)):
                    if word[i] == userguess:
                        wrd_underscores[i] = userguess
                print("Here are your remaining letters: ", wrd_underscores)
            else:
                print("your guess: ", userguess ,"is not a part of this word!")
                max_guesses -= 1

                if max_guesses == 5:
                    body()
                elif max_guesses == 4:
                    armright()
                elif max_guesses == 3:
                    armleft()
                elif max_guesses == 2:
                    head()
                elif max_guesses == 1:
                    legs()
                elif max_guesses == 0:
                    otherleg()

                print("guesses remaining: ",max_guesses)
        if "_" not in wrd_underscores:
                print("you win!" + "\U0001F3C6")
        else:
            print("game over" + "\u274C")
    else:
        print("end-")
    t.exitonclick()

hangmangame()

