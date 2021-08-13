# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def binarySearch(self,nums,s,e):
        if s>e:
            return None
        m = (s+e)//2
        head = TreeNode(nums[m])
        #print(head.val)
        head.left = self.binarySearch(nums,s,m-1)
        head.right = self.binarySearch(nums,m+1,e)
        
        return head
    
    def sortedArrayToBST(self, nums: List[int]) -> TreeNode:
        s = 0
        e = len(nums)
        return self.binarySearch(nums,s,e-1)
        
        
        