from random import randint

num=randint(1,20)

print("This program is a guessing game! There are only 3 chances to play this game.")



for i in range(3):
    guess=eval(input("Type your guess number between 1 and 20: "))
    if guess == num:
        print("Congratulations, You got it! ")
    elif guess <= num:
        print("Too Low, Try Again!")
    elif guess >= num:
        print("Too high, Try Again!")
    else:
        print("Invalid! Please try again.")

print("Game over!")
