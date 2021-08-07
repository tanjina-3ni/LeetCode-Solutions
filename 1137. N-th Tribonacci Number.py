class Solution:
    def tribonacci(self, n: int) -> int:
        if n<=1:
            return n
        first = 0
        second = 1
        third = 1
        for i in range(2,n):
            res = first + second + third
            first = second
            second = third
            third = res
        return third