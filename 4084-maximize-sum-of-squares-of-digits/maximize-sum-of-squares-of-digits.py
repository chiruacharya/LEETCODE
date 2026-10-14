class Solution:
    def maxSumOfSquares(self, num: int, sum: int) -> str:
        # COMPLETELY OWN SOLVED
        s = 0
        for i in range(num):
            s+=9
            if s>sum:
                break
        while s!=sum and s>0:
            s-=1
        print(s)
        if s == 0:
            return ""
        a = "9"*(s//9) + str(s%9)
        if len(a)<num:
            a+="0"*(num-len(a))
        if len(a)>num:
            a = a[:num - len(a)]
        return a
