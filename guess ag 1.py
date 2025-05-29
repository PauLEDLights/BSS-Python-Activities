from random import randint

print("This program is a guessing game! You only get 3 chances to play this game.")

for i in range(3):
    num=randint(1,20)
    print(num)
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
