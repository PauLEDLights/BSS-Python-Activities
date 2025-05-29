#Write a program that asks the user for an hour between 1 and 12,
#asks them to enter am or pm, and asks them how many hours into the future they want to go. 
#Print out what the hour will be that many hours into the future,
#printing am or pm as appropriate.
#points:

print("Time Travel Simulator!")

while True:
    swt = eval(input("AM (1) or PM (2)? \n"))
    if swt >= 3 or swt == 0:
        print("Invalid. Please type 1 for AM or 2 for PM. \n")
    elif swt == 1:
        break
    else:
        break
    
while True:
    time = eval(input("Set time (1-12): \n"))
    if time >= 13 and time <= 24:
        print("Hours 13-24(or 00:00) are only available in Military format.")
    elif time >= 25:
        print("12 hours only")
    else:
        break

while True:
    chtime = eval(input("How many hours do you want to skip? \n"))
    if chtime >= 13:
        print("Up to 12 hours only")
    else:
        break

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
    