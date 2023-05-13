# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy_head = ListNode()
        dummy_head.next = head
        cur = dummy_head

        while cur.next != None and cur.next.next != None: 
            # 奇数 cur.next.next != None
            # 偶数 cur.next != None
            # 但要先判断 cur.next 再判断 cur.next.next
            # 否则先判断 cur.next.next 如果 cur.next == None 会报错
            temp = cur.next             #  临时指针存1
            temp2 = cur.next.next.next  #  临时指针存3
            cur.next = cur.next.next    # cur 指向 2
            cur.next.next = temp        # 2 指向 1
            temp.next = temp2           # 1 指向 3
            cur = cur.next.next         # cur 移动两位

        return dummy_head.next





        
