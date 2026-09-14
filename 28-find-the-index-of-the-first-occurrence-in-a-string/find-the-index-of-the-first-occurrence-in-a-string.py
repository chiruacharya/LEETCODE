class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        # COMPLETELY OWN SOLVED
        if len(haystack)==len(needle ):
            if haystack == needle:
                return 0
            else: return -1
        for i in range(len(haystack )-len(needle )+1):
            print(haystack[i:i+len(needle)],i,len(needle))
            if haystack[i:i+len(needle)] == needle:
                return i
        return -1