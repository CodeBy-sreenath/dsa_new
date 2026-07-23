a=int(input("enter the first number"))
b=int(input("enter the second number"))
c=int(input("enter the third number"))
d=int(input("enter the fourth number"))
if a>b:
    if a>c:
        if a>d:
            print("larger is",a)
        else:
            print("larger is",d)
    else:
        print("largest is",c)
else:
    if b>c:
        if b>d:
            print("largest is",b)
        else:
            print("largest is",d)
    else:
        print("largest is",c)                            

