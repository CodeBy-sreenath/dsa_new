class Solution:
    def thirdLargest(self,nums):
        nums=list(set(nums))
        nums.sort(reverse=True)
        if len(nums)>=3:
            return nums[2]
        return nums[0]
print(Solution().thirdLargest([1,1,2,3,2]))    
            