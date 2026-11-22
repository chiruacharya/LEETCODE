class Solution:
    def checkString(self, s: str) -> bool:
        # COMPLETELY OWN SOLVED
        a = False
        for i in s:
            if i == "b":
                a = True
            if i =="a" and a == True:
                return False
        return True

