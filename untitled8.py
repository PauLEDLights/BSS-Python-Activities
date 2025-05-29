from random import randint

num=randint(1,20)

print("This program is a guessing game! There are only 3 chances to play this game.", num)



for i in range(3):
    guess=eval(input("Type your guess number between 1 and 20: "))
    if guess == num:
        pts = 0+1
        print("Congratulations, You got it! ")
        break
    else:
        pts = 0
        print("Wrong Number. Try again!")

if pts == 0:
    print("Game Over...")
else:
    print("Game Clear!")

