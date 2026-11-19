class Solution:
    def minimizeSum(self, nums: List[int]) -> int:
        # COMPLETELY OWN SOLVED
        nums.sort()
        a = len(nums)-2
        ans = float("inf")
        for i in range(3):
            ans = min(ans,max(nums[i:a+i])-min(nums[i:a+i]))
        return ans