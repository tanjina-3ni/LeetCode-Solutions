class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        s = 0
        e = len(numbers)-1
        l = []
        while s<=e:
            m = int((e-s)/2)
            if numbers[s]+numbers[e]==target:
                l.append(s+1)
                l.append(e+1)
                return l
            elif numbers[s]+numbers[e]>target:
                e = e - 1
            else:
                s = s + 1