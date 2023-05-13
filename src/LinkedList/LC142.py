# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        fast = head
        slow = head
        index_2 = head
        # 目标是当index1等于index2时，一定在环的入口

        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
            if fast is slow:  # 如果快指针与慢指针相遇
                index_1 = slow # 记录此时的相遇位置index1
                while index_1 is not index_2:  #如果此时index2 还不等于index1
                    index_2 = index_2.next     # index2 往前走
                    index_1 = index_1.next     # index1 往前走
                return index_1  #相遇时即是答案入口
