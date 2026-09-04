class Solution:
    def firstStableIndex(self, nums: list[int], k: int) -> int:
        # COMPLETELY OWN SOLVED
        answer = float("inf")
        index = float("inf")
        for i in range(len(nums)):
            temp = (max(nums[:i+1]) - min(nums[i:]))
            if temp <= k and temp<answer and i < index:
                
                answer = temp
                index = i
                print(answer,index)
        if index <= len(nums):
            return index
        else:return -1