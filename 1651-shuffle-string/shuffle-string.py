class Solution:
    def restoreString(self, s: str, indices: list[int]) -> str:
        # COMPLETELY OWN SOLVED
        l = [""]*len(s)
        for i,j in enumerate(indices):
            l[j] = s[i]
        return "".join(l)
