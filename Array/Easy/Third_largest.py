n=[10,13,15,10,9]
first_largest=-1
second_largest=-1
third_largest=-1
for i in n:
    if i>first_largest:
        third_largest=second_largest
        second_largest=first_largest
       
        first_largest=i
    if i>second_largest and i!=first_largest:
        third_largest=second_largest
        second_largest=i
    
    if i>third_largest and i!=first_largest and i!=second_largest:
            third_largest=i
print(third_largest)                    