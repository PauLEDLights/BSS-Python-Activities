from random import randint

num=randint(1,20)

print("This program is a guessing game! There are only 3 chances to play this game.", num)

pts = 0
pnt = 0

for i in range(3):    
    guess=eval(input("Type your guess number between 1 and 20: "))

    if guess == num:
        print("Congratulations, You got it! ")
        pts = +1
        pnt = +0
        
    else:
        print("Wrong Number. Try again!")
        pts = +0
        pnt = +1
        
if pts == 0 or pnt == 2:
    print("Game Over...")
elif pts == 2 and pnt == 0:
    print("Slay!")
else:
    print("Game Over...")

print(pts, pnt)
