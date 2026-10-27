class Solution:
    def createGrid(self, m: int, n: int) -> list[str]:
        # COMPLETELY OWN SOLVED
        l = []
        for _ in range(m-1):
            l.append("."+("#"*(n-1)))
        l.append("."*n)
        return l
