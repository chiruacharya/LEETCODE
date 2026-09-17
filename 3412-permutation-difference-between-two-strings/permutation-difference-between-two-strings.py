class Solution:
    def findPermutationDifference(self, s: str, t: str) -> int:
        # COMPLETELY OWN SOLVED
        d1 = {}
        d2 = {}
        for k , i in enumerate(s):
            d1[i]=k
        for k , i in enumerate(t):
            d2[i]=k
        count = 0
        for v in d1:
            count += abs(d1[v]-d2[v])
        return count