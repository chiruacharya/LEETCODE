class Solution:
    def maxNumberOfFamilies(self, n: int, reservedSeats: List[List[int]]) -> int:
        #COMPLETELY OWN SOLVED
        d = {}
        for i in reservedSeats:      
            d[i[0]]= []
        for i in reservedSeats:
            d[i[0]].append(i[1])
        count = 0
        for k , v in d.items():
            c1 = True
            c2 = True
            if 2 not in v and 3 not in v and 4 not in v and 5 not in v:
                count +=1 
                c1 = False
            if 4 not in v and 5 not in v and 6 not in v and 7 not in v and c1:
                count +=1 
                c2 = False
            if 6 not in v and 7 not in v and 8 not in v and 9 not in v and c2:
                count +=1 
        return count +abs((n-len(d))*2)