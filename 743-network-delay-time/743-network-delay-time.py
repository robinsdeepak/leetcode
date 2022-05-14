class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        
        if len(times) < n - 1:
            return -1
        
        inf = float('inf')
        
        d = [inf] * n
        d[k - 1] = 0
        
        mset = [False] * n
        
        mat = [[-1] * n for _ in range(n)]
        
        for u, v, w in times:
            mat[u - 1][v - 1] = w
            # print(u - 1, v - 1, w)
        
        
        for i in range(n):
            minDistId = -1
            
            for j in range(n):
                if not mset[j] and (minDistId == -1 or d[j] < d[minDistId]):
                    minDistId = j
            
            mset[minDistId] = True
            
            for j in range(n):
                if not mset[j] and mat[minDistId][j] != -1:
                    d[j] = min(d[j], d[minDistId] + mat[minDistId][j])
    
        
        ans = max(d)
        ans = -1 if ans == inf else ans
        return ans
