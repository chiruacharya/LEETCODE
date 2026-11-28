class Solution:
    def finalPrices(self, prices: list[int]) -> list[int]:
        # COMPLETELY OWN SOLVED
        l1 = []
        for i in range(len(prices)-1):
            c= True
            for j in prices[i+1:]:
                if j<=prices[i]:
                    l1.append(prices[i]-j)
                    c = False
                    break
            if c :
                l1.append(prices[i])
        l1.append(prices[-1])
        return l1
