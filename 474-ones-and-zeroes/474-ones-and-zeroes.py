from functools import lru_cache

class Solution:

    def findMaxForm(self, strs: List[str], m: int, n: int) -> int:
        return self.recursive_2(strs, m, n)
    
    def iterative(self, strs, m, n):
        dp = [[0] * (n + 1) for _ in range(m + 1)]
        
        for s in strs:
            c0 = s.count("0")
            c1 = len(s) - c0
            
            for i in range(m, c0 - 1, -1):
                for j in range(n, c1 - 1, -1):
                    dp[i][j] = max(dp[i][j], dp[i - c0][j - c1] + 1)
            
        return dp[m][n]
    
    def recursive(self, strs, m, n):
        ln = len(strs)
        inf = float('inf')
        
        @lru_cache(maxsize=None)
        def rec(i, c0, c1):
            if c0 < 0 or c1 < 0: return -inf
            if i == ln: return 0
            
            cc0 = strs[i].count("0")
            cc1 = len(strs[i]) - cc0
            
            return max(rec(i + 1, c0, c1), rec(i + 1, c0 - cc0, c1 - cc1) + 1)
            
        return rec(0, m, n)

    def recursive_2(self, strs, m, n):
        counter = Counter([(s.count('0'), s.count('1')) for s in strs])
        d = defaultdict(lambda: -1)
        
        def dfs(m, n, count):
            if d[(m, n)] >= count: return d[(m, n)]
            max_count = count
            d[(m, n)] = count
            
            for k, v in counter.items():
                if v <= 0: continue
                zeros, ones = k[0], k[1]
                if zeros <= m and ones <= n:
                    counter[k] -= 1
                    max_count = max(max_count, dfs(m - zeros, n - ones, count + 1))
                    counter[k] += 1
            return max_count        
        return dfs(m, n, 0)
        
    