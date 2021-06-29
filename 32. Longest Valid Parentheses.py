class Solution:
    def longestValidParentheses(self, s: str) -> int:
        stack = [-1]
        maxlength = 0
        
        for i in range(0,len(s)):
            if s[i]=='(':
                stack.append(i)
            else:
                stack.pop()
                if len(stack)==0:
                    stack.append(i)
                else:
                    x = stack.pop()
                    stack.append(x)
                    maxlength = max(maxlength, i - x)
        return maxlength
                    