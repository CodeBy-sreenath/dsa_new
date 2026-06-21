class Solution:
    def missing(self,nums):
        n=len(nums)
        expected_sum=n*(n+1)//2
        current_sum=sum(nums)
        missing_num=expected_sum-current_sum
        return missing_num
        
print(Solution().missing([9,6,4,2,3,5,7,0,1]))        