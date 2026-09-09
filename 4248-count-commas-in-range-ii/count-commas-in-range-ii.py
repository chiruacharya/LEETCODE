class Solution:
    def countCommas(self, n: int) -> int:
        # COMPLETELY OWN SOLVED
        if n < 1000:
            return 0
        answer = ((len(str(n))-1)//3)* n
        for i in range(((len(str(n))-1)//3),0,-1):
            answer-=  int("999"*i)
        return answer