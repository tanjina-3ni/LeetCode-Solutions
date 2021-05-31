class Solution:
    def sortSentence(self, s: str) -> str:
        s = list(s.split())
        s1 = ''
        j = 1
        i = 0
        while j<=len(s):
                if i==len(s):
                    i = 0
                if str(j) in s[i]:
                    s1 = s1 + s[i]
                    if j==len(s):
                        s1 = s1.replace(str(j),'')
                    else:
                        s1 = s1.replace(str(j),' ')
                    j = j + 1
                i = i + 1
        return s1