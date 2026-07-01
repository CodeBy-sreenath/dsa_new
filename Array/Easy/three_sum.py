class Solution:
    def three_sum(self,nums):
        nums.sort()
        result=[]
        for i in range(len(nums)-2):
            left=i+1
            right=len(nums)-1
            while left<right:
                if i>0 and  nums[i]==nums[i-1]:
                    continue
                totatl=nums[i]+nums[left]+nums[right]
                if totatl==0:
                    result.append([nums[i],nums[left],nums[right]])
                    while left<right and nums[left]==nums[left+1]:
                        left+=1
                    while left<right and nums[right]==nums[right-1]:
                        right-=1
                    left+=1
                    right-=1
                elif totatl<0:
                    left+=1
                else:
                    right-=1
        return result
s=Solution()
print(Solution().three_sum([-1,0,1,2,-1,-4]))                            

