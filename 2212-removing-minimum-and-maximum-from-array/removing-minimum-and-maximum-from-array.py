class Solution:
    def minimumDeletions(self, nums: List[int]) -> int:
        # COMPLETELY OWN SOLVED
        max_no = max(nums)
        min_no = min(nums)

        min_check = True
        max_check = True

        i = 0
        j=-1

        min_ans = 0
        max_ans = 0
        while min_check or max_check:
            if nums and abs(i)<len(nums) and nums[i] == min_no:
                min_ans = i+1
                nums = nums[i+1:]
                i = -1
                j=-1
                min_check = False
            if nums and abs(i)<len(nums)  and nums[i] == max_no :
                max_ans = i+1
                nums = nums[i+1:]
                i = -1
                j=-1
                max_check = False
            i+=1
            if nums and abs(j)<=len(nums)  and nums[j] == min_no :
                min_ans = abs(j)
                nums = nums[:j]
                j=0
                i=-1
                min_check = False
            if nums and abs(j) <=len(nums) and  nums[j] == max_no:
                max_ans = abs(j)
                nums = nums[:j]
                j=0
                i=-1
                max_check = False
            j-=1
            if not nums:
                break
        return min_ans  + max_ans 
