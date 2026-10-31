class Solution:
    def maximizeSum(self, nums: List[int], k: int) -> int:
        # COMPLETELY OWN SOLVED
        a = max(nums)
        return (((a+(k-1))*(a+(k-1)+1))//2) - ((a*(a-1)//2))