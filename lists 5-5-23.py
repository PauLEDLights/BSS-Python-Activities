#list
#empty list
#declared data in list
gayporn=[5, 3, 8.6, 9, "BAGUIO", 5, [4, 5, 6]]
#printing of list
print(gayporn)
#print without bracket w/ for loop
for items in gayporn:
    print(items)

#list
list = []

list=eval(input("Type your scores (Use comma between data): "))


print("My scores: ")
for items in list:
    print(items)

#list
#len-length of data inside list
#sum-total of all the data inside list
list=[]
list=eval(input("Input Socres (use comma in-between):" ))

average=sum(list)/len(list)

print("Average: ", average)

#indexing and slicing
list=[]
list=eval(input("Input Socres (use comma in-between):" ))
#use 0 for first, 1 for sec... -1 for last num, -2 second last num... :3 for first 3 nums
print("last number: ", list[3])

#max(list) and minimum(list)
list=[]
list=eval(input("Input Socres (use comma in-between):" ))

print("highest no.: ", max(list))
print("lowest no.: ", min(list))

list=[]
list=eval(input("Input Socres (use comma in-between):" ))

#Sorting List

sorted_list=sorted(list)

print("Sorted Data: ", sorted_list)

#Reversing list
reversed_list=sorted_list[::-1]

print("ReversedData: ", reversed_list)

