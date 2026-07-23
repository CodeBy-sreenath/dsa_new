print("CALCULATOR:")
a=int(input("enter the first number"))
b=int(input("enter the second number"))
op=input("enter the operation to perforom(enter the symbols like +,-,*,/,// ...)")
if op=='+':
    print(a+b)
elif op=='-':
    print(a-b)
elif op=='*':
    print(a*b)
elif op=='/':
    print(a/b)
else:
    print("no opeartion is possible")
                    