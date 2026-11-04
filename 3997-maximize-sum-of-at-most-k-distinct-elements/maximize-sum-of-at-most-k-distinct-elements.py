class Solution:
    def maxKDistinct(self, nums: List[int], k: int) -> List[int]:
        # COMPLETELY OWN SOLVED
        a = sorted(set(nums))
        return a[-k:][::-1]