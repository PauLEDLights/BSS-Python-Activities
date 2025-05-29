small = 0
big = 0
while True:
    input_num = eval(input("Insert Integer:"))

    if input_num == 0:
        break
    if input_num < small and input_num != 0 or input_num !=0 :
        small = input_num
    if input_num > big:
        big = input_num

dif = big - small
print("Smallest Value:", small)
print("Biggest Value:", big)
print("Difference between Smallest and Biggest =", dif)
        
