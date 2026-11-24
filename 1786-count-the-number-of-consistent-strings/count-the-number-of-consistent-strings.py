class Solution:
    def countConsistentStrings(self, allowed: str, words: List[str]) -> int:
        # COMPLETELY OWN SOLVED
        d = {}
        ans_count = 0
        for i in allowed:
            d[i]=None
        for i in words:
            for j in i:
                if j not in d:
                    ans_count -=1
                    break
            ans_count +=1
        return ans_count
