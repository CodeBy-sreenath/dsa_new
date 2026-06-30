class Solution:
    def longest(self,str):
        left=0
        seen=set()
        max_length=0
        for right in  range(len(str)):

            while str[right] in seen:
                seen.remove(str[left])
                left+=1
            seen.add(str[right])    
            max_length=max(max_length,right-left+1)
        return max_length
str="abcabcabc"
print(Solution().longest(str))            
