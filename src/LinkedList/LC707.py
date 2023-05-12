class Node (object) :
    def __init__ (self, val = 0, next = None):
        self.val = val
        self.next = next

class MyLinkedList:

    def __init__(self):
        self.head = Node()
        self.size = 0

    def get(self, index: int) -> int:
        if index < 0 or index >= self.size:
            return -1 
        cur = self.head.next
        while index:
            cur = cur.next
            index -=1
        return cur.val

    def addAtHead(self, val: int) -> None:
        new_node = Node(val)
        new_node.next = self.head.next
        self.head.next = new_node
        self.size +=1 

    def addAtTail(self, val: int) -> None:
        cur = self.head
        while (cur.next):
            cur = cur.next
        new_node = Node(val)
        cur.next = new_node
        self.size +=1


    def addAtIndex(self, index: int, val: int) -> None:
        if index < 0:
            return
        elif index == self.size:
            self.addAtTail(val)
            return
        elif index > self.size:
            return

        new_node = Node(val)
        cur = self.head
        while index:
            cur = cur.next
            index -=1
        new_node.next = cur.next
        cur.next = new_node
        self.size +=1

    def deleteAtIndex(self, index: int) -> None:
        if index < 0 or index >= self.size:
            return
        cur = self.head
        while index:
            cur = cur.next
            index -=1
        cur.next = cur.next.next
        self.size -=1

        



# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)
