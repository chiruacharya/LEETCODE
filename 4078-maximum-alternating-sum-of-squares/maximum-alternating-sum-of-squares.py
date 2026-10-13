class Solution:
    def maxAlternatingSum(self, nums: List[int]) -> int:
        # COMPLETELY OWN SOLVED
        for i in range(len(nums)):
            nums[i] =  nums[i]**2
        n = sorted(nums)
        if len(n) %2==0:
            return  sum(n[len(n)//2:]) - sum(n[:len(n)//2])
        else:
            return  (sum(n[len(n)//2:-1]) - sum(n[:len(n)//2]))+n[-1]