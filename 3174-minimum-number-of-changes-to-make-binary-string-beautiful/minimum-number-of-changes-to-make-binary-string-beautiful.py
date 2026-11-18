class Solution:
    def minChanges(self, s: str) -> int:
        # COMPLETELY OWN SOLVED
        c = 0
        i = 0
        for _ in range(len(s)//2):
            if s[i] != s[i+1]:
                c+=1
            i+=2
        return c
            