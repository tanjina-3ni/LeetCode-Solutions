class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        l = nums1 + nums2
        l.sort()
        s = 0
        e = len(l)-1
        m = int((s+e)/2)
        if (e+1)%2!=0:
            return l[m]
        else:
            return (l[m]+l[m+1])/2

