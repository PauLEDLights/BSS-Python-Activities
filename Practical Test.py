# Make a Point of Sales System Program
# Points = 5
# Edited post-checking. Working code is shown

E1 = 440
E2 = 1790
E3 = 3590
P1 = E1
P2 = E2
P3 = E3

print("\t *Primogem Store* \t")
print("Items")
print("Code \t Product \t     Price")
print("P1  \t Primogemsx240 \t 440Php")
print("P2  \t Primogemsx960 \t 1790Php")
print("P3  \t Primogemsx1920\t 3590Php \n")


odr = eval(input("How many Orders do you want to make?\n"))
total = 0
for i in range(odr):
    dsp = input("Type the Product Code \n")
    amt = eval(input("Type the quantity\n"))
    if dsp == "P1" or dsp == "p1":
        total_amt=E1*amt
        print("P1 Primogemsx240", total_amt, "Php \n")
        total=total_amt+total
    elif dsp == "P2" or dsp == "p2":
        total_amt=E2*amt
        print("P2 Primogemsx960",E2*amt, "Php \n")
        total=total_amt+total
    elif dsp == "P3" or dsp == "p3":
        total_amt=E3*amt
        print("P3 Primogemsx1920", E3*amt, "Php \n")
        total=total_amt+total
    elif dsp == "Skin" or dsp == "skin":
        print("You unlocked the secret menu! Please contact this number for more details!")
        print("Phone Num: 09XX-XXX-XXXX")
    else:
        print("Invalid \n")
    
    if i == odr:
        break
    else:
        print("Order", i+1, "Done \n")

print("Total Amount:", total, "Php")
pay=eval(input("Payment Amount:"))
if total<=pay:
    print("Change:", pay-total)
else:
    print("Insufficient Amount")

print("\nThank you for using Primogems Store!")