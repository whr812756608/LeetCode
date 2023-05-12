class ListNode:
    # python ListNode class
    # __init__ 传入参数： self， val， next = None
    def __init__ (self,val = 0 , next = None):
    # __init__ function 功能实现加self
        self.val = val     
        self.next = next

class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:

        # 使用 dummy_head 模版
        # 先创建 dummy_head，ListNode(next = head)，next指向链表的原head
        dummy_head = ListNode(next = head)
        
        # 创建指针指向dummy_head， 因为我们想修改下一个节点，
        # 指针指向想修改节点的上一个节点才能进行修改操作
        cur = dummy_head
        
       
        while cur.next != None:  # 判断下一节点不为空，因为要读取下一个节点的val， 否则会报错
            if cur.next.val == val: #读取cur.next的val
                cur.next = cur.next.next # 删除操作，让原本指向下一个节点的指针
                                         # 指向下下个节点，cur.next.next 
            else:
                cur = cur.next       # 如果不需要删除，则让指针指向下一节点

        return dummy_head.next       # 最后返回dummy_head的下一节点，
                                     # 即原链表的头节点
