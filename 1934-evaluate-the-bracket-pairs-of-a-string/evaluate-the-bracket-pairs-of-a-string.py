class Solution:
    def evaluate(self, s: str, knowledge: list[list[str]]) -> str:
        # COMPLETELY OWN SOLVED
        d = {}
        for i in knowledge:
            d[i[0]] = i[1]
        def find(n):
            if n in d:
                return d[n]
            else:
                return "?"
        l=0
        r=0
        a=""
        for i,v in enumerate(s):
            if v =="(":
                l = i+1
                a=a+s[r:l-1]
            if v ==")":
                r = i+1
                a = a+find(s[l:r-1])
        return a+s[r:]
