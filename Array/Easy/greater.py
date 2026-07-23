a=int(input("enter the first number"))
b=int(input("enter the second number"))
c=int(input("enter the third number"))
if a<b:
    if a<c:
        print(a,"is smaller")
    else:
        print(c,"is smaller")
else:
    if b<c:
        print(b,"is smaller")
    else:
        print(c,"is smaller")                