# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        #neetcode
        dummy = ListNode(0, head)
        prev, curr = dummy, head
        
        while curr and curr.next:
            # 1) 선언 => save pointers
            nxtPair = curr.next.next
            second = curr.next
            
            # 2) next들을 옮겨주기 => reverse this pair
            second.next = curr
            curr.next = nxtPair
            prev.next = second
            
            # 3) 좌표 shift => update pointers ** prev->curr!
            prev = curr #!!!curr가 nxtPair 바로 뒤자리로 위에서 이동했기때문에 prev에댜가 curr을 넣어줄 수 있는것!!!
            curr = nxtPair
            
        return dummy.next
        
        
        '''
        # <<<<<내가 1시간 반동안 고민한 코드>>>>> ==> 어떻게해서든 풀긴풀어서 통과함!!! 이제는 다른 풀이 보고 최적화시키기!!
        if not head:
            return head
        
        if not head.next:
            return head
        
        # 위에 두 개 합친 코드 구현하기!!!
        dummy = ListNode(next = head)
        
        prev, curr = head, head.next
        dummy.next = curr
        
        while True:
            
            nxt = curr.next
            
            curr.next = prev
            
            prev.next = nxt
            
            # if nxt == None:
            #     return dummy.next
            # else:
            #     if nxt.next == None:
            #         return dummy.next
            #     else:
            #         prev.next = nxt.next #### 이거를 못해서!!!!
            #         prev, curr = nxt, nxt.next

            if nxt == None or nxt.next == None:
                return dummy.next
            else:
                prev.next = nxt.next #### 이거를 못해서!!!!
                prev, curr = nxt, nxt.next
        '''

                
                
            
        
