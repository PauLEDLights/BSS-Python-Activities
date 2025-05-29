#sent to: mcprado@rtu.edu.ph
#Labide, Paul John L. - Perfect Number Checker

while True:
    num = eval(input("Enter a Positive Integer (Or 0 to Exit): "))
    if num == 0:
        print("Goodbye!")
        break
    else:
        divisors_sum = 0
        for i in range (1, num):
            check = num % i
            if check == 0:
                print(i, "has no remainder")
                check2 = (i + divisors_sum)
                print(i + divisors_sum)
                
        print(check2)    
        
    if check2 == num:
        print(num, " is a perfect number.")
    else:
        print(num, " is not a perfect number.")