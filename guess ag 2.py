from random import randint

num=randint(1,20)

print("This program is a guessing game! There are only 3 chances to play this game.")

pts = 0

for i in range(3):
    guess=eval(input("Type your guess number between 1 and 20: "))
    if guess == num:
        print("Congratulations, You got it! ")
        goal = pts + 1
        break
    elif guess <= num:
        print("Too Low, Try Again!")
        goal = 0
    elif guess >= num:
        print("Too high, Try Again!")
        goal = 0
    else:
        print("Invalid! Please try again.")
        goal = 0


if goal == 0:
    print("Game over!")
else:
    print("Game clear!")
