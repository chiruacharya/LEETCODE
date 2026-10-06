class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        # COMPLETELY OWN SOLVED
        # d = {}
        # for i in s:
        #     if i in d:
        #         d[i] += 1
        #     else:
        #         d[i] = 1
        # ans = 0
        # if "(" in d:
        #     ans = d["("]
        # if ")" in d:
        #     ans = abs(ans-d[")"])
        # return ans

        s1 = []
        s2 = []
        for i in range(len(s)):
            if s[i] == "(":
                s1.append(i)
            else:
                s2.append(i)

        score = 0
        while True:
            if s1:
                if s2:
                    if s1[-1]>s2[-1]:
                        score +=1
                        s1.pop()
                    else:
                        s1.pop()
                        s2.pop()
                else:
                    return score+len(s1)
            else:
                return score+len(s2)
