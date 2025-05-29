#while loop
temp = 0
while temp !=-1000:
    temp = eval(input("Enter temperature (-1000 to )"))
    if temp != -1000:
        print("Farenheit: ", 9/5*temp+32)        
    else:
        print("See ya!")