def move_zero(nums):
    i=0
    while i<len(nums):
        if nums[i]==0:
            nums.pop(i)
            nums.append(0)
            i+=1
        else:
            i+=1
    return nums
print(move_zero([0, 1, 0, 3, 12]))            
          