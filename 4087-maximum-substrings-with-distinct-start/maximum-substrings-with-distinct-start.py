class Solution:
    def maxDistinct(self, s: str) -> int:
        # COMPLETELY OWN SOLVED
        d = {}
        ans = 0
        for i in s:
            if i not in d:
                ans+=1
                d[i]=1
                
        return ans

