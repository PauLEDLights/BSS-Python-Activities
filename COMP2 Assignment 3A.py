# Write a program that asks the user for their name and how many times to print it.
# The program should print out the user’s name the specified number of times.
print("Obssessed Lover Calls Your Name Simulator\n")
name = input ("Enter what name your lover should call you: \n")
obs = eval(input("Enter how many times you want them to call your name: \n"))
for i in range(obs):
    print(name, "!", sep="")