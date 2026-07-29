#5 Take a list of numbers sort it without using built-in methods like sort,sorted
n=int(input("enter the length of the list"))
lst=[]
for i in range(n):
  value=int(input(f"enter the element {i+1} :"))
  lst.append(value)
print("original list :",lst)
for i in range(len(lst)):
  for j in range(i+1,len(lst)):
    if lst[i]>lst[j]:
      lst[i],lst[j]=lst[j],lst[i]
print("reversed list :",lst)      



  
