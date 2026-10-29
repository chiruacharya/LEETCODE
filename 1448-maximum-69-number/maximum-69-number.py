class Solution:
    def maximum69Number (self, num: int) -> int:
        # COMPLETELY OWN SOLVED
        max_no = num
        s = str(num)
        for i in range(len(s)):
            if s[i] == "6":
                s=s[:i] +"9"+s[i+1:]
                max_no = max(max_no,int(s))
                s = s[:i] +"6"+s[i+1:]
            else:
                s = s[:i] +"6"+s[i+1:]
                max_no = max(max_no,int(s))
                s = s[:i] +"9"+s[i+1:]
        return max_no
