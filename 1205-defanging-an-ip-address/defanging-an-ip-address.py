class Solution:
    def defangIPaddr(self, address: str) -> str:
        # COMPLETELY OWN SOLVED
        a = ""
        for i in address:
            if i == ".":
                a += "[.]"
            else:
                a+= i
        return a