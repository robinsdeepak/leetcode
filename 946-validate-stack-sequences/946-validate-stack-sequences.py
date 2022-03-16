class Solution:
    def validateStackSequences(self, pushed: List[int], popped: List[int]) -> bool:
        stack = []
        ptr = 0
        for x in pushed:
            stack.append(x)
            
            while len(stack) and stack[-1] == popped[ptr]:
                stack.pop()
                ptr += 1
        
            
        return len(stack) == 0
