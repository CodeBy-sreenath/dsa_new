
stack=[]
while True:
    print("enter 1 for push")
    print("enter 2 for pop")
    print("enter 3 for peek")
    print("enter 4 for dispaly")
    print("enter 5 for exit")
    choice=int(input(" enter the choice "))
    match choice:
        case 1:
            x=int(input("enter the element"))
            stack.append(x)
            print("element is successfully added")
        case 2:
            if len(stack)==0:
                print("underflow")
            else:
                print("stack is popped",stack.pop())
        case 3:
            if len(stack)==0:
                print("stack is empty no element to display")
            else:
                print(stack[-1])
        case 4:
            print(stack)
        case 5:
            print("exiting....")
            break              
                        
