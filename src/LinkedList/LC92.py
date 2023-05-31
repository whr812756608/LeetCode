#Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        dummy_head = ListNode(next = head)
        p0 = dummy_head
        
        for _ in range (left-1):    #  left-1 will arrive the previous node of left
            p0 = p0.next            # p0=p0.next, move 1 postion 
        
        cur = p0.next               # cur is on the left node
        pre = None                  # set pre = None,  same as reverse linkedlist I

        for _ in range(right-left+1):  # total right-left +1 elements need to reverse
                                       # when right = left, there is one elements            
                                       # (right, left points to same element)
            nxt = cur.next             # same for reverse linkedlist I
            cur.next = pre             
            pre = cur
            cur = nxt

        p0.next.next = cur 
        p0.next = pre                # CANNOT change the order of these two line
                                     # Need to find the origin position of p0.next.next
                                     # if we set p0.next = pre frist, p0.next will change!
        return dummy_head.next
