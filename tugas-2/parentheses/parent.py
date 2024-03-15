class Solution:
    def __init__(self):
        self.stack = []
    def removeOuterParentheses(self, s: str) -> str:
        res = ""
        for i, c in enumerate(s):
            if c == "(":
                self.stack.append(i)
            if c == ")":
                start_i = self.stack.pop()
                if not len(self.stack): 
                    res += s[start_i+1:i]
        return res