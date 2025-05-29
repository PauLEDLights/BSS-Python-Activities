# A lot of cell phones have tip calculators. Write one. 
# Ask the user for the price of the meal and the percent tip they want to leave.
# Then print both the tip amount and the total bill with the tip included.

MP = eval (input ("Enter the meal price \n"))
TP = eval (input ("Enter tip percentage (%) \n"))
print ("Tip: ", (TP/100)*MP)
print ("\nTotal: ", MP + (TP/100)*MP)