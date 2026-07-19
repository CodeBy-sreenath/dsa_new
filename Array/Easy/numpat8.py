n=5
count=15
for i in range(1,n+1):
    for j in range(i):
        print(count,end=' ')
        count-=1
    print()    