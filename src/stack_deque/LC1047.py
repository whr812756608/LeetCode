class Solution:
    def removeDuplicates(self, s: str) -> str:
        stack = []

        for c in s:
            if not stack or c != stack[-1]:  # 判定为空集或者当前遍历元素与栈顶元素不同
                stack.append(c)              # 入栈
            else:
                stack.pop()                  # 否则pop 消消乐

        return "".join(stack)
