class Solution:
    def sumCounts(self, nums: List[int]) -> int:
        
        s = 0
        i = 0
        k = 1
        while  k<=len(nums):
            s += len(set(nums[i:i+k]))**2
            if (i+k) == len(nums):
                i=-1
                k+=1
            i+=1
        return s

            
