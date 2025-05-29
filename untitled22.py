#jak-en-poy
from random import choice
#choice for opponent's pick
game=["bato", "papel", "gunting"]

PPoints = 0
OPoints = 0

for i in range(5):
    player=input("Take a pick: bato, papel, gunting (lowercase only) ")
    computer_opponent=choice(game)
    print(computer_opponent)

    if computer_opponent == player:
        print("draw!")
    elif computer_opponent == "bato":
        if player == "papel":
            print("win!")
            PPoints = PPoints + 1 
        elif player == "gunting":
            print("lose!")
            OPoints = OPoints + 1
    elif computer_opponent == "papel":
        if player == "gunting":
            print("win!")
            PPoints = PPoints + 1 
        elif player == "bato":
            print("lose!")   
            OPoints = OPoints + 1
    elif computer_opponent == "gunting":
        if player == "bato":
            print("win!")
            PPoints = PPoints + 1 
        elif player == "papel":
            print("lose!")
            OPoints = OPoints + 1
            
print("Your Points: ", PPoints)
print("Opponent's Points: ", OPoints)

if PPoints>=OPoints:
    print("Winner: Player!")
elif PPoints==OPoints:
    print("Tie!")
else:
    print("Winner: Opponent!")