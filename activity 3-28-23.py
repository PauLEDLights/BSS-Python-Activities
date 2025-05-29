#user is asked to input password
pw=12345
tr=0
att=0
mx = 5
while tr > 0:
    
    acc = eval(input("Please Enter Password: "))
    if acc == pw:
        print("Password Correct. Logging in...")
        break
    else:
        tr -= 1
        if tr == 0:
        print("Password Incorrect.")
        print("All attempts used. You are locked.")
        print("Attempts left:", )

    if att == 5:
        
        break
        
