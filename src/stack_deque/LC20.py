class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        for c in s:
            if c == "{":
                stack.append("}")
            elif c == "[":
                stack.append("]")
            elif c == "(":
                stack.append(")")
            elif not stack or c != stack[-1]:  #重点条件，not stack 指右括号多（左右pop完了，新来一个右括号），c！=stack 指左右括号不匹配
                return False 
            else:
                stack.pop()
        return True if not stack else False
