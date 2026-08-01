def plusone(nums):
    for i in range(len(nums)-1,-1,-1):
        if nums[i]<9:
            nums[i]=nums[i]+1
            return nums
        nums[i]=0
    nums.insert(0,1)
    return nums 
nums=[9,9,9]
print(plusone(nums))   
        