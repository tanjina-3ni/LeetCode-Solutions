class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        s = s.split()
        if len(s)==0:
            length = 0
        else:    
            length = len(s[len(s)-1])
        return length

