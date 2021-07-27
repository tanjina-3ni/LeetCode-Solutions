class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        l1 = list(set(nums1))
        l2 = list(set(nums2))
        l3 = []
        if len(l1)<len(l2):
            for i in range(len(l1)):
                if l1[i] in l2:
                    l3.append(l1[i])
        else:
            for i in range(len(l2)):
                if l2[i] in l1:
                    l3.append(l2[i])
        return l3
        

