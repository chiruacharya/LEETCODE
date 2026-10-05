class Solution:
    def scoreOfParentheses(self, s: str) -> int:
        # stack = []
        # b = False
        # c = 0
        # score = 0
        # for i in range(len(s)):
        #     if s[i] == "(":
        #         stack.append(s[i])
        #         # score +=c
        #         b = False
        #         c = 0
        #     if b and s[i] == ")":
        #         score *=2
        #         c *=2
        #     elif s[i] == ")":
        #         b = True
        #         score +=1
        #         c = 1
        #     # if i == len(s)-1 :
        #     #     score +=c
        # return score



        # stack = []
        # b = False
        # c = 0
        # score = 0
        # temp = 0
        # k = False 
        # for i in range(len(s)):
        #     if s[i] == "(":
        #         if not stack :
        #             temp += score
        #             score = 0
        #         stack.append(i)
        #         # score +=c
        #         b = False
        #         c = 0
        #         a = 0
        #     if b and s[i] == ")":
                
        #         if stack[-1]==(i-a):
        #             score += c*2 -c
        #             a+=2
        #             stack.pop()
        #         else:
        #             score *=2
        #             # k = True

        #         c *=2
        #     elif s[i] == ")":
        #         a=3
        #         stack.pop()
        #         b = True
        #         score +=1
        #         c = 1
        # # if k:
        # #     return score + temp
        # # else:
        # return score + temp
        stack = []
        score = 0

        for i in range(len(s)):
            if s[i] == "(":
                stack.append(score)
                score = 0

            else:
                if score == 0:
                    score = 1
                else:
                    score *= 2

                score += stack.pop()

        return score