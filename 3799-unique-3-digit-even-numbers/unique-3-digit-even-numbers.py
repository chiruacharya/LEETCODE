class Solution:
    def totalNumbers(self, digits: List[int]) -> int:
        
        # d = {}
        # ec=0
        # zero_count = 0
        # for i in digits:
        #     if i ==0:
        #         zero_count+=1
        #         continue
        #     if i%2==0:
        #         ec+=1
        #     if i in d:
        #         d[i]+=1
        #     else:
        #         d[i]=1
        # rep =1
        # for v in d.values():
        #     if v >1:
        #         for i in range(1,v+1):
        #             rep *=i
        # if ec:
        #     return ((len(digits)-1) * (len(digits)-2) * ec)//rep
        # else:
        #     return 0
        freq = [0] * 10
        for d in digits:
            freq[d] += 1
        ans = 0
        for first in range(1, 10): 
            for second in range(10):
                for last in range(0, 10, 2):
                    if freq[first] == 0:
                        continue
                    freq[first] -= 1
                    if freq[second] == 0:
                        freq[first] += 1
                        continue
                    freq[second] -= 1
                    if freq[last] > 0:
                        ans += 1
                    freq[second] += 1
                    freq[first] += 1

        return ans
