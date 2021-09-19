class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        i=0
        while i<len(nums):
            res = target-nums[i]
            if res in nums and nums.index(res)!=i:
                return [i,nums.index(res)]
            i += 1
        