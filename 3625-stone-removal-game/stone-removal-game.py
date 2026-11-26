class Solution:
    def canAliceWin(self, n: int) -> bool:
        # COMPLETELY OWN SOLVED
        for i in range(10,0,-1):
            n -=i
            if n<0:
                if i%2==0:
                    return False
                else: return True