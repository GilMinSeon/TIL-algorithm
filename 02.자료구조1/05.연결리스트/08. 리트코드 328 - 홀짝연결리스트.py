'''
혼자 못 푼 문제!
꼭 복습하기!!
'''

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return None
        
        odd = head
        even = head.next
        even_head = head.next
        
        # while 종료 조건이 중요! odd가 아닌 even으로 해야함
        # 그리고 even의 head를 가지고 있어야 odd마지막과 even을 연결하니까! 떠올렸어야 하는 지점
        
        # 1) [1], [1,2]일때 even.next는 null이니까 while문 안들어가고 바로 종료
        # 2) [1,2,3] 일때 적어도 even.next = 3이니까 적어도 even.next.next = null할 수 있다! None.next하면 오류나기 때문에 적어도 even.next는 유효한 값이어야함
        #    그리고 odd가 앞이기 때문에(odd.next = even), 무조건 odd.next.next도 가능! 왜냐면 odd.next즉 even이 null값이 아니므로
        #    내가 .next를 할때 . 앞에 있는 객체가 Null이 아니어야함!
        
        while even and even.next:
            odd.next = odd.next.next
            even.next = even.next.next
            
            odd = odd.next
            even = even.next
        
        odd.next = even_head
        
        return head
