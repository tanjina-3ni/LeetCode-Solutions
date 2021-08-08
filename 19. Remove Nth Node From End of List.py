# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        current = head
        length = 0
        while current:
            length += 1
            current = current.next
        
        n = length - n
        
        length = 0
        if n==0:
            head = head.next
            return head
        current = head
        while length != n-1:
            length += 1
            current = current.next 

        current.next = current.next.next

        return head
            
        
            
            
            
            