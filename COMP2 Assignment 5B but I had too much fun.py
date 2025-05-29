#Write a program that asks the user for an hour between 1 and 12,
#asks them to enter am or pm, and asks them how many hours into the future they want to go. 
#Print out what the hour will be that many hours into the future,
#printing am or pm as appropriate.

print("Time Travel Simulator!")
print("I know you want to change the time, but time can only go forward :( \n")

while True:
    swt = eval(input("AM (1) or PM (2)? \n"))
    if swt >= 3 or swt == 0:
        print("Invalid. Please type 1 for AM or 2 for PM. \n")
    elif swt == 1:
        print("Set to AM")
        break
    else:
        print("Set to PM")
        break
    
while True:
    time = eval(input("Set time (1-12): \n"))
    if time >= 13 and time <= 24:
        print("Hours 13-24(or 00:00) are only available in Military format.")
    elif time >= 25:
        print("There are only 24 hours in this planet, I don't know which planet is that from.")
    else:
        print("Time set to", time)
        break

chtime = eval(input("How many hours do you want to skip? \n"))
if swt == 1:
    timesk = time + chtime
    if timesk >= 13:
        print("\n", timesk - 12, "PM", sep="")
    else:
        print("\n", timesk, "AM", sep="")        
elif swt == 2:
    timesk = time + chtime
    if timesk >= 13:
        print("\n", timesk - 12, "AM", sep="")
    else:
        print("\n", timesk, "PM", sep="")  
    
else:
    print("How the hell did you passed over the pervious checks? (ʘ言ʘ╬)")
    