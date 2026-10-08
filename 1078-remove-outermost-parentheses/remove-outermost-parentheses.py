class Solution:
    def removeOuterParentheses(self, s: str) -> str:
        stack = ""
        ans = ""
        k=0
        for i in s:
            stack= stack +str(i)
            if i == "(":
                k+=1
            else:
                k-=1
            if i ==")" and k==0:
                ans += stack[1:-1]
                stack = ""
                k=0
        return ans

        # COMPLETELY OWN SOLVED
        
        