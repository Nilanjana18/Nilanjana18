#guess the correct number 
#on guessing the correct number you win!
from random import randrange
n=randrange(10)#in this step we are taking any random number in the specified range and if it matches with the user input we will win the game.
while True:
    v=int(input())
    if n==v:
        print("You Win!")
        print("Congratulations!")
        break
    print("Smaller" if (n>v) else "Bigger")
