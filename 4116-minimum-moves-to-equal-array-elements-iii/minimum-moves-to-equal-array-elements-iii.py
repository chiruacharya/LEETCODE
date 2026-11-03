class Solution:
    def minMoves(self, nums: List[int]) -> int:
        # COMPLETELY OWN SOLVED
        return (max(nums)*len(nums)) - sum(nums)