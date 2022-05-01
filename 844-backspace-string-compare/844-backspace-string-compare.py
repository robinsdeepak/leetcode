class Solution:
    def process(self, s):
        stack = []
        for c in s:
            if c != '#':
                stack.append(c)
            elif len(stack):
                stack.pop()
        return "".join(stack)
    
    def backspaceCompare(self, s: str, t: str) -> bool:
        return self.process(s) == self.process(t)
