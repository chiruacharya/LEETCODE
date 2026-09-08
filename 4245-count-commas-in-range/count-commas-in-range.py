class Solution:
    def countCommas(self, n: int) -> int:
        # COMPLETELY OWN SOLVED
        if n <1000:
            return 0
        answer = n-1000+1
        return answer