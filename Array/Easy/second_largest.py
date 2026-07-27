n=[11,10,12,8,7,17,0]
first_largest=-1
second_largest=-1
for i in n:
    if i>first_largest:
        second_largest=first_largest
        first_largest=i
    if i>second_largest and i!=first_largest:
        second_largest=i
print(second_largest)            
        