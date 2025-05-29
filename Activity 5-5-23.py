#jak-en-poy
from random import choice
#choice for opponent's pick
game=["BATO", "PAPEL", "GUNTING"]

PPoints = 0
OPoints = 0

for i in range(5):
	print("ROUND", i+1)
	player=input("Take a pick: BATO, PAPEL, GUNTING (All caps only): ")
	computer_opponent=choice(game)
	print("Your opponent picked:",computer_opponent)

	if computer_opponent == player:
    		print("draw!")
	elif computer_opponent == "BATO":
    		if player == "PAPEL":
        			print("win!")
        			PPoints = PPoints + 1
    		elif player == "GUNTING":
        			print("lose!")
        			OPoints = OPoints + 1
	elif computer_opponent == "PAPEL":
    		if player == "GUNTING":
        			print("win!")
        			PPoints = PPoints + 1
    		elif player == "BATO":
        			print("lose!")   
        			OPoints = OPoints + 1
	elif computer_opponent == "GUNTING":
    		if player == "BATO":
        			print("win!")
        			PPoints = PPoints + 1
    		elif player == "PAPEL":
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
