a=int(input("enter the first number"))
b=int(input("enter the second number"))
c=int(input("enter the third number"))
if a>b:
    if a>c:
        print("larger is",a)
    else:
        print("larger is",c)
else:
    if b>c:
        print("larger is",b)
    else:
        print("larger is",c)                