"""
1
3 5
7 9 11
13 15 17 19
"""
n=5
count=1
for i in range(1,n+1):
    for j in range(i):
        print(count,end=' ')
        count+=2
    print()    