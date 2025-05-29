# Write a program that asks the user how many Fibonacci numbers to print
# and then prints that many.
print("Fibonacci Generator/n")
obs = eval(input("Enter how many Fibonacci numbers you want to generate: \n"))
first = 0
second = 1
print("\nSequence Start")
print(first)
print(second)
for i in range(1,obs-1):
    third = first + second
    print(third)
    first,second=second,third
    