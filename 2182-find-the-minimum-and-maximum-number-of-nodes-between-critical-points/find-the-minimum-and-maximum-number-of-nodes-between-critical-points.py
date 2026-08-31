# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def nodesBetweenCriticalPoints(self, head: Optional[ListNode]) -> List[int]:
        # COMPLETELY OWN SOLVED
        curr = head.next
        index = 1
        prev = head
        l1 = []
        ans = []
        while curr.next:
            if prev.val<curr.val and curr.val >curr.next.val:
                l1.append(index)
            if prev.val>curr.val and curr.val <curr.next.val:
                l1.append(index)
            index+=1
            prev = prev.next
            curr = curr.next

        if len(l1)>=2:
            temp = l1[1]-l1[0]
            min_dist = temp
            for i in range(2,len(l1)):
                if l1[i]-l1[i-1] < temp:
                    min_dist = l1[i]-l1[i-1]
                    temp = l1[i]-l1[i-1]

            ans.append(min_dist)
            ans.append(l1[-1]-l1[0])
            return ans
        else:return [-1,-1]

        