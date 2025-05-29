#Write a multiplication game program for kids. 
#The program should give the player ten randomly generated multiplication questions to do 
#(between 1 and 10 only). 
#After each, the program should tell them whether they got it right or wrong 
#and the correct answer. At the end of the program, display the player's score out of ten.
#points: 
from random import randint
print("Multiplication Game!")
print("(Please answer in numbers only)")

cpoints=0
for i in range(10):
    QA = randint(1,10)
    QB = randint(1,10)
    cor = QA*QB
    print("Question No. ", i+1, sep="")
    print(QA, " x ", QB, sep="")
    ans=eval(input("Type your answer: \n"))
    
    if ans == cor: 
        print("Correct Answer! \n")
        cpoints= cpoints + 1
       
    elif ans != cor: 
        print("Wrong Answer! \n")
        print("The correct answer is ", cor, "!\n", sep="")
        cpoints= cpoints + 0

    else:
        print("Invalid Answer! Please answer in numerical characters.")
        print("This answer will be considered wrong, sorry!\n")
        
print("Game Finished!")
print("Score: ", cpoints, "/", 10, sep="")