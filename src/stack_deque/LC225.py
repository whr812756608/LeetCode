class MyStack:

    def __init__(self):
        self.queue = deque()


    def push(self, x: int) -> None:
        return self.queue.append(x)


    def pop(self) -> int:
        if self.empty():
            return 

        for _ in range(len(self.queue)-1):
            val = self.queue.popleft()
            self.queue.append(val)
        return self.queue.popleft()


    def top(self) -> int:
        if self.empty():
            return 
        return self.queue[-1]
        # for _ in range(len(self.queue)-1):
        #     val = self.queue.popleft()
        #     self.queue.append(val)
        # val = self.queue.popleft()
        # self.queue.append(val)
        # return val

    def empty(self) -> bool:
        return True if not self.queue else False



# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()
