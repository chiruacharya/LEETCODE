class Solution:
    def smallerNumbersThanCurrent(self, nums: list[int]) -> list[int]:
        # COMPLETELY OWN SOLVED
        d = {}
        a = sorted(nums)
        ans = []
        for i in range(len(a)):
            if a[i] not in d:
                d[a[i]]= len(a[:i])
        for i in nums:
            ans.append(d[i])
        return ans