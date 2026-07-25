class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for i in tokens:
            if i not in "+-*/":
                stack.append(i)
            else:
                y = int(stack.pop())
                x = int(stack.pop())
                match i:
                    case "+":
                        res = x + y
                    case "-":
                        res = x - y
                    case "*":
                        res = x * y
                    case "/":
                        res = int(x / y)
                stack.append(res)
        return int(stack.pop())
        