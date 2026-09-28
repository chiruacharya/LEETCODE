class Solution:
    def maxDepth(self, s: str) -> int:
        # COMPLETELY OWN SOLVED
        count,answer = 0,0
        for i in s:
            if i == "(":
                count += 1
                answer = max(answer,count)
            if i == ")":
                count -= 1
        return answer

            