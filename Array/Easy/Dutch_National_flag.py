class Solution:
    def nationalFlag(self,nums):
        mid=0
        low=0
        high=len(nums)-1
        while mid<high:
            if nums[mid]==0:
                nums[low],nums[mid]=nums[mid],nums[low]
                low+=1
                mid+=1
            elif nums[mid]==1:
                mid+=1
            else:
                high-=1
                    

    