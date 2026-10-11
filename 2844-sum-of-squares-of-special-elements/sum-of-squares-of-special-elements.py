class Solution:
    def sumOfSquares(self, nums: List[int]) -> int:
        # COMPLETELY OWN SOLVED
        answer = 0
        l = len(nums)
        for i, k in enumerate(nums):
            if l%(i+1)==0:
                answer +=k*k
        return answer