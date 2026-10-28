class Solution:
    def totalMoney(self, n: int) -> int:
        # COMPLETELY OWN SOLVED
        amt = 0
        if n<=7:
            for i in range(n):
                amt+= i+1
        else:
            a,r = divmod(n,7)
            print(a,r)
            amt+= (28*a)
            for i in range(a):
                amt+=7*i
            print(amt)
            for i in range(1,r+1):
                amt+= a+i
                print(amt,a,i)
        return amt