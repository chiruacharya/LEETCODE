class Solution:
    def reverseParentheses(self, s: str) -> str:
        # COMPLETELY OWN SOLVED
        l = []
        a = s
        c = 0
        for i,v in enumerate(s):
            if v =="(":
                l.append(i-c)
            if v ==")":
                a = a[:l[-1]]+a[l[-1]+1:i-c][::-1] + a[i-c+1:]
                c+=2
                l.pop()
        return a
