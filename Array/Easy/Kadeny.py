class Solution:
    def kadneys(self,nums):
        current_sum=nums[0]
        max_sum=nums[0]
        for num in nums:
            current_sum=max(num,num+current_sum)
            max_sum=max(current_sum,max_sum)
        return max_sum
nums = [-2,1,-3,4,-1,2,1,-5,4]
print(Solution().kadneys(nums))        