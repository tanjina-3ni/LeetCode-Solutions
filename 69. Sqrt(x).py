class Solution:
    def mySqrt(self, x: int) -> int:
        l = len(str(x))
        n = int(l/2) + 1
        while 1:
            n = int(((x/n) + n )/2)
            if n*n == x or (n*n<x and (n+1)*(n+1)>x):
                return n
                
                    