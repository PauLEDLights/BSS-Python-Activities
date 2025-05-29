##Point of Sale System

#displaying of text

print("              Services")
print("Code    Service                 Price")
print("[A]     Hair Cut                P100.00")
print("[B]     Hair Cut with Blowdry   P200.00")
print("[C]     Brazillian Blowout      P1500.00")

#declaration of variable with input
#variable = eval(input("TEXT"))

service=eval(input("How many services do you want to avail? "))

#for loop
#for i in range(number):  for i in range(3)

total_amount=0
for i in range(service):
    #eval is for number inputs only
    code=input("Type the code: ")
    quantity=eval(input("Type the quantity of the service: "))
    
  
    ##double quote ("") for string
    if code == "A" or code == "a": 
        serv_total=quantity*100
        print(quantity, " Hair Cut P", serv_total)
        total_amount= serv_total + total_amount
       
    elif code == "B" or code == "b": 
        serv_total=quantity*200
        print(quantity, " Hair Cut with Blowdry P", serv_total)
        total_amount= serv_total + total_amount
    
    elif code == "C" or code == "c": 
        serv_total=quantity*1500
        print(quantity, " Brazillian Blowout P", serv_total)
        total_amount= serv_total + total_amount
    
    else:
        print("Invalid Code")


print("Total Amount: ",total_amount)
payment=eval(input("Payment Amount: "))
if payment<total_amount:
    print("Insufficient Amount\n")
    for i in range(999):
        print("Total Amount: ",total_amount)
        payment=eval(input("Payment Amount: "))
        if payment<total_amount:
            print("Insufficient amount \n")
            continue
        elif payment>=total_amount:
            print("Change: ",payment-total_amount)
            break
else:
    print("Change: ",payment-total_amount)

