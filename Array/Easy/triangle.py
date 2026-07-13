a=int(input("enter the side1"))
b=int(input("enter the side2"))
c=int(input("enter the side3"))
if a==b:
    if a==c:
        print("equilateral triangle")
    else:
        print("isosilus triangle")
else:
    if a==c or b==c:
        print("isosilus triangele")
    else:
        print("scalene")    
