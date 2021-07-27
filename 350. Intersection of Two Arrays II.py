class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        l1 = len(nums1)
        l2 = len(nums2)
        l3 = []
        if l1<=l2:
            for i in range(l1):
                if nums1[i] in nums2:
                    nums2 = nums2[:nums2.index(nums1[i])] + nums2[nums2.index(nums1[i])+1:]
                    l3.append(nums1[i])
        else:
            for i in range(l2):
                if nums2[i] in nums1:
                    nums1 = nums1[:nums1.index(nums2[i])] + nums1[nums1.index(nums2[i])+1:]
                    l3.append(nums2[i])
        return l3
        