n=5
for i in range(1,n+1):
    for space in range(n-i):
        print(" ",end='')
    for j in range(1,i):
        print(j,end='')
    
    for k in range(i,0,-1):
        print(k,end='')
    print()
for i in range(n-1,0,-1):
    for space in range(n-i+1):
        print(" ", end='')
    for j in range(1,i):
        print(j,end='')
    for k in range(i,0,-1):
        print(k,end='')
    print()            
