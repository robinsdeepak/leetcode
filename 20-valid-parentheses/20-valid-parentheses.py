class Solution:
    def isValid(self, s: str) -> bool:
        m = {'{': '}', '(': ')', '[': ']'}
        
        st = []
        
        for char in s:
            if len(st) and m.get(st[-1]) == char:
                st.pop()
            else:
                st.append(char)
        
        return not st

