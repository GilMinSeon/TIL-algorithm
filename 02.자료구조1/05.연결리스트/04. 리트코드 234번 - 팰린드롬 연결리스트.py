'''
3가지 풀이법 순차적으로 이해! 다시 
'''

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        # 3) <파이썬 알고리즘 인터뷰>
        rev = None
        slow = fast = head
        
        while fast and fast.next:
            fast = fast.next.next
            rev, rev.next, slow = slow, rev, slow.next
            
        if fast:
            slow = slow.next
            
        while rev and rev.val == slow.val:
            slow, rev = slow.next, rev.next
        return not rev
        
        
        
#         # 2) fast & slow pointer<neetcode>
#         fast = head
#         slow = head
        
#         while fast and fast.next:
#             fast = fast.next.next
#             slow = slow.next

#         prev = None
#         while slow:
#             tmp = slow.next
#             slow.next = prev
#             prev = slow
#             slow = tmp
        
#         print(prev)
#         # prev가 중간지점 기준으로 뒤집은 연결리스트!
#         left, right = head, prev
#         while right:
#             if left.val != right.val:
#                 return False
#             left = left.next
#             right = right.next
#         return True
        
        
        
        
#        # 1) 배열 풀이
#         arr = []
#         while head:
#             arr.append(head.val)
#             head = head.next
            
#         l, r = 0, len(arr)-1
        
#         while l <= r:
#             if arr[l] != arr[r]:
#                 return False
            
#             l += 1
#             r -= 1
#         return True
