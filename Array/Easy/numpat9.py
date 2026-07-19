"""
54321
65432
76543
87654
98765
"""
n=5 
count=5
for i in range(1,n+1):
    for j in range(count,i-1,-1):
        print(j,end='')
    count+=1
    print()    