def pivot(nums):
    left_sum=0
    right_sum=0
    for i in range(len(nums)):
        for j in range(i):
            left_sum+=nums[j]
        for j in range(i+1,len(nums)):
            right_sum+=nums[j]
        if left_sum==right_sum:
            return i
    return -1
print(pivot( [1, 7, 3, 6, 5, 6]))            
            