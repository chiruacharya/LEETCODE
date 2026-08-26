class Solution:
    def shortestBeautifulSubstring(self, s: str, k: int) -> str:
        # COMPLETELY OWN SOLVED
        i = 0
        j = k
        c = 1
        l1 = []

        while j-i <=len(s):
            if j>len(s):
                if l1:
                    return min(l1)
                else:
                    return ""
            a = s[i:j]
            count = 0
            for found in a:
                if found =="1":
                    count +=1
            if count == k:
                l1.append(a)
                if len(a)>len(l1[0]):
                    l1.pop()
                    return min(l1)

            if j==len(s) and j-i<len(s):
                i = 0
                j = k+c
                c+=1
            else:
                i+=1
                j+=1