class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        n = int(len(nums)/2)
        s = list(map(int, set(nums)))
        for i in range(0,len(s)):
            if nums.count(s[i])> n:
                break
        return s[i]