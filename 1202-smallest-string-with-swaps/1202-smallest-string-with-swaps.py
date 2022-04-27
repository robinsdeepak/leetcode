class Solution:
    def smallestStringWithSwaps(self, s: str, pairs: List[List[int]]) -> str:
        n = len(s)
        g = [[] for _ in range(n)]
        
        for i, j in pairs:
            g[i].append(j)
            g[j].append(i)
        
        visited = set()
        
        def dfs(x, st):
            st.append(x)
            for y in g[x]:
                if y not in visited:
                    visited.add(y)
                    dfs(y, st)
        
        idxArr = []
        
        for i in range(n):
            if i not in visited:
                st = []
                visited.add(i)
                dfs(i, st)
                if len(st): idxArr.append(st)
        
        letters = list(s)
        
        for arr in idxArr:
            si = sorted(arr)
            sl = sorted([s[i] for i in si])
            for i, c in zip(si, sl):
                letters[i] = c
        
        return "".join(letters)


        