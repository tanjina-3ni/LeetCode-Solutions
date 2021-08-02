# bottom up approach
class Solution:
        
    def getMaximumGenerated(self, n: int) -> int:
        nums = [-1]*(n+1)
        
        for i in range(0,n+1):
            if i<=1:
                nums[i] = i
                
            if i%2==0:
                nums[i] = nums[i//2]
            else:
                nums[i] = nums[i//2] + nums[(i//2)+1]
            #print(nums)
        return max(nums)