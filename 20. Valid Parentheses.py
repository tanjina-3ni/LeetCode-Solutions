class Solution:
    def isValid(self, s: str) -> bool:
        i = 0
        stack = []
        if s[len(s)-1]=='(' or s[len(s)-1]=='{' or s[len(s)-1]=='[':
            return 0
        while i<len(s):
            if s[i]=='(':
                stack.append(1)
            elif s[i]=='{':
                stack.append(2)
            elif s[i]=='[':
                stack.append(3)
            else:
                if len(stack)==0:
                    return 0
                x = stack.pop()
                if (s[i]==')' and x!=1) or (s[i]=='}' and x!=2) or (s[i]==']' and x!=3):
                    return 0
            i = i + 1
        if len(stack)==0:
            return 1
        else:
            return 0