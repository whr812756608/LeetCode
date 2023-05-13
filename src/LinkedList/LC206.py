# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        pre = None
        cur = head
        while cur:
            nxt = cur.next
            cur.next = pre
            pre = cur 
            cur = nxt
        return pre

 # 递归法
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        def reverseList(pre,cur):
            if not cur:
                return   
            nxt = cur.next
            cur.next = pre
            return reverseList(cur,nxt)
        
        return reverseList(None,head)
            
        
