class Solution:
    def minimumSum(self, num: int) -> int:
        # COMPLETELY OWN SOLVED
        l1 = [int(x) for x in str(num)]
        l1.sort()
        return int(str(l1[0])+str(l1[-1])) + int(str(l1[1])+str(l1[-2]))