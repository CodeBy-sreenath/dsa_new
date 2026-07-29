#4 Take a list that containing duplicate values write a program to remove the duplicate and print the remaining values without using set() method
n=int(input("enter the length of the list"))
lst=[]
lst1=[]
for i in range(n):
  value=input(f"enter the element {i+1} :")
  lst.append(value)
print("list with duplicate elements",lst
      )  

for item in lst:
  if item not in lst1:
    lst1.append(item)
print("list without duplicate elements :",lst1)      