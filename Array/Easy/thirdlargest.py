def third(nums):
    first=-1
    second=-1
    third=-1
    for i in nums:
        if i>first:
            third=second
            second=first
            first=i
        elif i>second and i!=first:
            third=second
            second=i
        elif i>third and i!=first and i!=second:
            third=i

    return third
nums=[8,9,3,0,2]
print(third(nums))            