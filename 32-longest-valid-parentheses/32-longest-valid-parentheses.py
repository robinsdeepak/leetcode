class Solution:
    def longestValidParentheses(self, s: str) -> int:
        st = []
        ans = 0
        for i in range(len(s)):
            ch = s[i]
            if st and st[-1][0] == '(' and ch == ')':
                st.pop()
                curr = i - st[-1][1] if st else i + 1
                ans = max(ans, curr)
            else:
                st.append((ch, i))
        return ans
