present = eval(input("Enter Current Time "))
swt = (input("AM (1) or PM(2)? "))
ts = eval(input("Skip how many hours? "))

futuref = (present+ts) % 12
if futuref == 0:
    futuref = 12
   
    
if swt == "1":
    future = present + ts
    if future <= 12:
        futureswt = "PM"
    else:
        futureswt = "AM"
elif swt == "2":
    future = present + ts
    if future <= 12:
        futureswt = "AM"
    else:
        futureswt = "PM"

print("New Time: ", future, futureswt, sep="")

    