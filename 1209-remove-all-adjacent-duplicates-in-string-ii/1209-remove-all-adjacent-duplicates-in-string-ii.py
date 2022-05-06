class Solution:
    def removeDuplicates(self, s: str, k: int) -> str:
        if not s: return s
        
        st = [[s[0], 1]]
        for i in range(1, len(s)):
            if not st or st[-1][0] != s[i]:
                st.append([s[i], 1])
            else:
                if st[-1][1] == k - 1:
                    for i in range(k - 1): 
                        st.pop()
                else:
                    st.append([s[i], st[-1][1] + 1])
        return "".join(map(lambda x: x[0], st))
