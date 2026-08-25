def match(list1,list2):
    new=[]
    if len(list1)!=len(list2):
        print("no operation possible")
    else:
        for i in range(len(list1)):
            new.append(list1[i]+list2[i])
        return new
list1=[1,2,3]
list2=[4,5,6]
print(match(list1,list2))        
