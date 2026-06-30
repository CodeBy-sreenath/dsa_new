class Solution:
    def two_sum(self,nums,target):
        seen={}
        for i,num in enumerate(nums):
            complement=target-num
            if complement in seen:
                return [seen[complement],i]
            seen[num]=i
        return []    
nums = [2, 7, 11, 15]
target = 9

print(Solution().two_sum(nums, target))    