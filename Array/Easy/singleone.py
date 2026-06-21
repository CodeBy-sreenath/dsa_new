class Solution:
    def single(self,nums):
        result=0
        for num in nums:
            result^=num
        return result
print(Solution().single([4,1,1,2,2]))        
