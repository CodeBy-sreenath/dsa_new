"""
1
21
123
4321
12345
"""
n=5
for i in range(1,n+1):
    if i%2==1:
        for j in range(1,i+1):
            print(j,end=' ')
        print()
    else:
        for j in range(i,0,-1):
            print(j,end=' ')
        print()            