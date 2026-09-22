class Solution:
    def longestPalindrome(self, s: str) -> int:
        # COMPLETELY OWN SOLVED
        d = {}
        for i in s:
            if i in d:
                d[i]+=1
            else:
                d[i]=1

        count = 0
        for k,v in d.items():
            if v>1:
                count+=(v//2)*2
        if len(s)==count:
            return count
        else:
            return count+1
