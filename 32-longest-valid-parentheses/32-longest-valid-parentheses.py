class Solution:
    def longestValidParentheses(self, s: str) -> int:
        left, right, ans = 0, 0, 0
        
        loops = [(0, len(s), 1), (len(s) - 1, -1, -1)]
        
        for start, end, step in loops:
            left, right = 0, 0
            for i in range(start, end, step):
                if s[i] == '(':
                    left += 1
                else:
                    right += 1

                if left == right:
                    ans = max(ans, 2 * right)

                if (step == 1 and right > left) or (step == -1 and left > right):
                    left, right = 0, 0
            
        
        return ans
