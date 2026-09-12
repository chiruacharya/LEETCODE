class Solution:
    def convertToBase7(self, num: int) -> str:
        # PARTIALY OWN SOLVED
        if num == 0:
            return "0"
        a = ""
        check = False
        if num<0:
            check = True
            num = abs(num)
        while num:
            digit = num%7
            a+=str(digit)
            num = num//7
        a = a[::-1]
        if check:
            return "-"+a
        return a