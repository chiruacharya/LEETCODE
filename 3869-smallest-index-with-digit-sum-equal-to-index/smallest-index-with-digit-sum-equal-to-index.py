class Solution:
    def smallestIndex(self, nums: List[int]) -> int:
        # COMPLETELY OWN SOLVED
        
        for i in range(len(nums)):
            answer = 0
            for j in str(nums[i]):
                answer +=int(j)
            if i == answer:
                return i
        return -1


