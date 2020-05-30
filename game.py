import random
import os
from time import sleep
from words import word
from display_parts import hang
choice = random.choice(word)
right = ['_']*len(choice)
wrong = []
chance = len(choice)+ 4
print('==========================================================================')
print("Lets start the game")
print("You have {} chances".format(chance))

def time():
    for i in range(3):
        print('.',end=" ")
        sleep(.3)
    print()
def update():
    for i in right:
        print(i, end =" ")
    print()

update()
while True:
    print('======================================================================')
    letter = input("Guess the letter : ")
    print("Checking your guess")
    time()
    if letter in choice:
        index = 0
        for i in choice:
            if i == letter:
                right[index] = letter
            index +=1
        print("Your guess is right")
        update()
        print("Wrong guesses ", wrong)



    else:
        if letter not in wrong:
            wrong.append(letter)
            print("Sorry!!! wrong guess")
            hang(len(wrong))
            print("Wrong guesses ", wrong)

        else:
            print("This is wrong guess and you entered it already")
    if '_'  not in right:
        print("YOU WON '_' ")
        break
    if len(wrong) >= 4:
        print("YOU LOSE")
        break


