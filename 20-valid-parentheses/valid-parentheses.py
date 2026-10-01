class Solution:
    def isValid(self, s: str) -> bool:
        # OWN SOLVED
        dict1 = {"(":")","[":"]","{":"}"}
        a = "([{"
        l1 = []
        if len(s)<=1:
            return False
        for i in s:
            if i in a:
                l1.append(i)
            elif len(l1) == 0:
                return False
            elif i == dict1[l1[-1]]:
                l1.pop()
            else:
                return False
            
        
        if len(l1) == 0:
            return True
        else:
            return False