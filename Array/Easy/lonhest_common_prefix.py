class Solution:
    def longest(self,strs):
        prefix=strs[0]
        for s in strs[1:]:
            while not s.startswith(prefix):
                prefix=prefix[:-1]
                if not prefix:
                    return ""
        return prefix
s=Solution()
print(Solution().longest(['flower','flight','flow']))    
            