class Solution:
    def remove(self,nums,val):
        k=0
        for i in range(len(nums)):
            if nums[i]!=val:
                nums[k]=nums[i]
                k+=1
        return k
s=Solution()
nums=[3,2,2,3]
val=3
print(s.remove(nums,val))            