class Solution:
    def missingMultiple(self, nums: List[int], k: int) -> int:
        # COMPLETELY OWN SOLVED
        temp = k
        while True:
            if temp in nums:
                temp+=k
                continue
            return temp