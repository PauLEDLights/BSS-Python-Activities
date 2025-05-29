#points: 4
from random import randint

num=randint(1,20)

print("This program is a guessing game! There are only 3 chances to play this game.", num)



for i in range(3):
    guess=eval(input("Type your guess number between 1 and 20: "))
    if guess == num:
        goal = 0+1
        print("Congratulations, You got it! ")
        break
    elif guess <= num and i<2:
        print("Too Low, Try Again!")
        goal = 0
    elif guess >= num and i<2:
        print("Too high, Try Again!")
        goal = 0
    else:
        print("Wrong Number! It's ", num, "!", sep="")
        goal = 0
if goal == 0:
    print("Game Over...")
else:
    print("Game Clear!")
