class Solution:
    def minimumSumSubarray(self, nums: List[int], l: int, r: int) -> int:
        # COMPLETELY OWN SOLVED
        # i = 0 
        # j = l
        # k = r
        # a1 = float("inf")
        # a2 = float("inf")
        # while j <= len(nums):
        #     if sum(nums[i:j])>0:
        #         a1 = min(a1,sum(nums[i:j]))
        #     print(a1,"a1")
        #     i+=1
        #     j+=1
        # i=0
        # while k <= len(nums):
        #     if sum(nums[i:k])>0:
        #         a2 = min(a2,sum(nums[i:k]))
        #     i+=1
        #     k+=1
        #     print(a2,"a2")
        # if min(a1,a2)< ((10**5) +1) :
        #     return min(a1,a2)
        # else:return -1
        a1 = float("inf")
        for j in range(l,r+1):
            i = 0
            while j <= len(nums):
                if sum(nums[i:j])>0:
                    a1 = min(a1,sum(nums[i:j]))
                print(a1,"a1")
                i+=1
                j+=1
        if a1< ((10**5) +1) :
            return a1
        else:return -1