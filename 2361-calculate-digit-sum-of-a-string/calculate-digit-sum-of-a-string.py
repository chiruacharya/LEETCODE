class Solution:
    def digitSum(self, s: str, k: int) -> str:
        # COMPLETELY OWN SOLVED
        def dsum(n,a):
            if len(n)<=a:
                return n
            n1 = ""
            t = 1
            ans = 0
            print(n,a)
            i =0
            while i <len(n):
                
                if t<=a :
                    ans+=int(n[i])
                    print(ans,"aaaaaa",i,n[i],t)
                else:
                    print("hi")
                    n1 = n1+str(ans)
                    print(n1)
                    t=0
                    ans =0
                    i-=1
                t+=1
                i+=1
            n1 = n1+str(ans)
            if len(n)>a:
                return dsum(n1,a)
            
        return dsum(s,k)


