exp=input("enter the expression")
stack=[]
balanced=True
pairs={
    ')':'(',
    '}':'{',
    ']':'['
}
for ch in exp:
    if ch in '({[':
        stack.append(ch)
    elif ch in ')}]':
        if len(stack)==0:
            balanced=False
            break
        top=stack.pop()
        if top!=pairs[ch]:
            balanced=False
            break
if len(stack)!=0:
    balanced=False
if balanced:
    print("balanced")
else:
    print("not balanced")               

        