def search_insert(nums,target):
    for i in range(len(nums)):
        if nums[i]==target:
            return i
        if nums[i]>target:
            return i

nums=[1,3,5,6]
target=2
print(search_insert(nums,target))                

    
