n=int(input("enter the number"))
stack=[]
while n>0:
    bin=n%2
    stack.append(bin)
    
    n=n//2
while stack:
    print(stack.pop(),end='')

   