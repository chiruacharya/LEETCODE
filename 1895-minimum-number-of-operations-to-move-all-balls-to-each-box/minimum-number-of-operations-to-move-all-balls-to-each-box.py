class Solution:
    def minOperations(self, boxes: str) -> List[int]:
        # COMPLETELY OWN SOLVED
        l1 = [i for i in range(len(boxes)) if boxes[i] == "1"]
        ans = []
        for i in range(len(boxes)):
            a = 0
            for j in l1:
                a += abs(i - j)
            ans.append(a)
        return ans
        