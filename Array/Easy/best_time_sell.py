class Solution:
    def bestTime(self,nums):
        min_price=float('inf')
        max_price=0
        for num in nums:
            min_price=min(min_price,num)
            max_price=max(max_price,num-min_price)
        return max_price
nums=[7,1,5,3,6,4]
s=Solution()
print(s.bestTime(nums))        