"""
123454321
 1234321
  12321
   121
    1
   121
  12321
 1234321
123454321
"""
n=5
for i in range(n,1,-1):
    for space in range(n-i):
        print(" ",end='')
    for j in range(1,i):
        print(j,end='')
    for k in range(i,0,-1):
        print(k,end='')
    print()
for i in range(1,n+1):
    for space in range(n-i):
        print(" ",end='')
    for j in range(1,i):
        print(j,end='')
    for k in range(i,0,-1):
        print(k,end='')
    print()                
