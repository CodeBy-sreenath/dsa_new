a=int(input("enter the first number"))
b=int(input("enter the second number"))
c=int(input("eneter the third number"))
if a>b:
    if a<c:
        print("second largest is",a)
    elif b>c:
        print("second largest is",b)
else:
    if b<c:
        print("second largest is ",b)
    elif a>c:
        print("second largest is",a)
    else:
        print("second largest is",c)    

             
