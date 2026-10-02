class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        # COMPLETELY OWN SOLVED
        if num == 1:
            return True
        i = 0
        j = num
        while i<j:
            mid = (i+j)//2
            a = mid*mid
            if a == num:
                return True
            if a<num:
                i = mid+1
            else:
                j = mid
        return False