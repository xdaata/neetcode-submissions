class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        si = {"+", "-", "*", "/"}
        for i in tokens:
            if i not in si:
                stack.append(int(i))
            else:
                y = stack.pop()
                x = stack.pop()
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
        return stack.pop()
        