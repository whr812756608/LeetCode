# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy_head = ListNode(next = head)
        fast, slow = dummy_head,dummy_head
       
        '''
        while 循环写法，注意是 n + 1 > 0 （或者 while n 大于等于0）
        while n + 1 > 0:
           fast = fast.next
           n -=1 
        '''
        # for 循环写法，走n+1步直接 in range （n+1）
        for _ in range(n+1):
            fast = fast.next
        
        while fast != None:
            fast = fast.next
            slow = slow.next
        slow.next = slow.next.next

        return dummy_head.next
