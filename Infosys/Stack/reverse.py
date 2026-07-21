stack=[]
s=input("enter the string")
rev=''
for i in s:
    stack.append(i)
while stack:
    rev=rev+stack.pop()
print(rev)    


    