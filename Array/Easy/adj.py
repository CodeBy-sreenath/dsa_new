#17 consecutive duplicate checker:write a program that iterate through a list and check if the list conatain any adjacent duplicate elements
n=int(input("enter the length of list1"))
list1=[]
new=[]
for i in range(n):
  value=input(f"enter the element{i+1} :")
  list1.append(value)
for i in range(len(list1)-1):
  if list1[i]==list1[i+1]:
    print("True")
    break
else:
  print("False")



