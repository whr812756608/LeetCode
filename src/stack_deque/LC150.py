class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []


        for i in range(len(tokens)):
            if tokens[i] not in ["+","-","*","/"]:
                stack.append(int(tokens[i]))
            else:
                right = stack.pop() # 先pop的元素在运算符右边
                left  = stack.pop() # 后pop的元素在左边
                if tokens[i] == "+":
                    stack.append(left + right)
                elif tokens[i] == "-":
                    stack.append(left - right)
                elif tokens[i] == "/":
                    stack.append(int(left/right))
                else:
                    stack.append(left * right)
        return stack.pop()
