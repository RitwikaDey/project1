list1 = []
n = int(input("Enter number of elements : "))
print("Enter the numbers in the list")
for i in range (0,n): 
    elem = int(input())  
    list1.append(elem)
print("Positive numbers are:")
for num in list1:
    if num >= 0: 
       print(num, end = " ")
