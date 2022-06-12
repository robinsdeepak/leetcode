from functools import lru_cache

class Solution:
    def distributeCookies(self, cookies: List[int], k: int) -> int:
        ans = float('inf')
        childs = [0] * k
        
        @lru_cache(maxsize=None)
        def rec(c, mx):
            if c == len(cookies):
                nonlocal ans
                ans = min(mx, ans)
                return
            
            for j in range(k):
                childs[j] += cookies[c]
                rec(c + 1, max(mx, childs[j]))
                childs[j] -= cookies[c]
        
        rec(0, 0)
        return ans
