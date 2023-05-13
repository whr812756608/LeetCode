# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        fast = head
        slow = head
        
        # 快指针走两步
        # 慢指针走一步
        # 链表长度为偶数时，当fast走到null上，slow一定在中间
        # 链表长度为奇数时，当fast走到null-1上，slow一定在中间
        # 等价于 fast.next 为空

        while fast and fast.next:     # 
            fast = fast.next.next
            slow = slow.next
        return slow
