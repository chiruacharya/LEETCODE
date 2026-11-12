class Solution:
    def longestMonotonicSubarray(self, nums: List[int]) -> int:
        a = 1
        b = 1
        ans = 1

        for i in range(1, len(nums)):
            if nums[i] > nums[i-1]:
                a += 1
                b = 1

            elif nums[i] < nums[i-1]:
                b += 1
                a = 1

            else:
                a = 1
                b = 1

            ans = max(ans, a, b)

        return ans