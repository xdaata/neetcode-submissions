class Solution:
    def isValid(self, s: str) -> bool:
        dct = {
            ')': '(',
            ']': '[',
            '}': '{'
        }
        stack = []
        for i in s:
            if i not in dct:
                stack.append(i)
            else:
                if not stack or stack.pop() != dct[i]:
                    return False
        if stack:
            return False
        
        return True



            
        