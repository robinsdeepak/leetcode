class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        if len(trust) < n-1:
            return -1
        
        trust_to = [0 for _ in range(n + 1)]
        trusted_by = [0 for _ in range(n + 1)]
        
        for i, j in trust:
            trust_to[i] += 1
            trusted_by[j] += 1
        
        for i in range(1, n + 1):
            if trust_to[i] == 0 and trusted_by[i] == n - 1:
                return i
        return -1
