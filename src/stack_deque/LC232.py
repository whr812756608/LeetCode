class MyQueue:

    def __init__(self):
        self.stack_in  =  []
        self.stack_out = []


    def push(self, x: int) -> None:
        return self.stack_in.append(x)


    def pop(self) -> int:
        if self.empty():
            return None
        if self.stack_out:
            return self.stack_out.pop()
        else:
            while self.stack_in:
                val = self.stack_in.pop()
                self.stack_out.append(val)
            return self.stack_out.pop()


    def peek(self) -> int:
        val = self.pop()
        self.stack_out.append(val)
        return val


    def empty(self) -> bool:
        return False if self.stack_in or self.stack_out else True
