class Solution:
    def digitFrequencyScore(self, n: int) -> int:
        # COMPLETELY OWN SOLVED
        hm ={}
        for i in str(n):
            if i == "0":
                continue
            if i in hm:
                hm[i] += 1
            else:
                hm[i] = 1
        ans = 0
        for k,v in hm.items():
            ans+=v*int(k)
        return ans