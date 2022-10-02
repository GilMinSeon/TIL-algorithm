# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # 2) neetcode
        prev, curr = None, head
        
        while curr:
            nxt = curr.next
            
            curr.next = prev
            
            prev, curr = curr, nxt
            
        return prev
        
        
        '''
        # 1) 책 - 반복구조로 뒤집기
        node, prev = head, None
        
        while node:
            next, node.next = node.next, prev
            prev, node = node, next
            
        return prev
        '''
            
