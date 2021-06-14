class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        if num==1:
            return 1
        s = 1
        e = num>>1
        while s<=e:
            mid = s + int((e-s)/2)
            root = mid*mid
            if root == num:
                return 1
            elif root<num:
                s = mid + 1
            else:
                e = mid - 1
        return 0