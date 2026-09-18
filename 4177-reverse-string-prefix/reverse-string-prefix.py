class Solution:
    def reversePrefix(self, s: str, k: int) -> str:
        # COMPLETELY OWN SOLVED
        return s[:k][::-1]+s[k:]