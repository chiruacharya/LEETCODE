class Solution:
    def hammingWeight(self, n: int) -> int:
        # COMPLETELY OWN SOLVED
        return sum([int(x) for x in bin(n)[2:] if x == "1"])