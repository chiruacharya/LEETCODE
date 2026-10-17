class Solution:
    def maxFreqSum(self, s: str) -> int:
        # COMPLETELY OWN SOLVED
        d = {0:0}
        d1 = {0:0}
        for i in s:
            if i in ["a","e","i","o","u"]:
                if i in d:
                    d[i]+=1
                else:d[i]=1
            else:
                if i in d1:
                    d1[i]+=1
                else:d1[i]=1
        return max(d.values()) + max(d1.values())
