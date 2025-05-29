# Write a program that asks the user to enter three numbers
# (use three separate input statements)
# Create variables called total and average that hold the sum and average of the three numbers
# and print out the values of total and average

num1 = eval (input ("Enter a number (1) \n"))
num2 = eval (input ("Enter a number (2) \n"))
num3 = eval (input ("Enter a number (3) \n"))
sum = num1 + num2 + num3
ave = sum/3
print ("Sum: ", sum)
print ("\nAverage: ", ave)
