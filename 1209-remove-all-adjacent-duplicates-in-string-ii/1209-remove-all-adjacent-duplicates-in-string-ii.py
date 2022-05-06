class Solution:
    def removeDuplicates(self, s: str, k: int) -> str:
        if not s: return s
        
        st = [[s[0], 1]]
        for i in range(1, len(s)):
            if not st or st[-1][0] != s[i]:
                st.append([s[i], 1])
            else:
                st[-1][1] += 1
                if st[-1][1] == k:
                    st.pop()
                
        return "".join(map(lambda x: x[0] * x[1], st))

