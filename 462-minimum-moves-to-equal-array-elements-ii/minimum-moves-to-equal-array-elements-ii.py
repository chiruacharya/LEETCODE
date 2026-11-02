class Solution:
    def minMoves2(self, nums: list[int]) -> int:
        # COMPLETELY OWN SOLVED
        # s = 0
        # l = 0
        # for i in nums:
        #     if i>0:
        #         s +=i
        #         l+=1
        # avg_no = s//l
        # ans = 0
        # for i in nums:
        #     ans += abs(avg_no - i)
        # return ans
        # COMPLETELY OWN SOLVED
        s = sorted(nums)
        i = 0
        j = len(nums)-1
        ans = 0
        while j>=i:
            ans += abs(s[i] - s[j])
            i+=1
            j-=1
        return ans

