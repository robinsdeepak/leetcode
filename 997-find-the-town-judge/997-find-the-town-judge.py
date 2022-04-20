class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        trust_to = {i : 0 for i in range(1, n + 1)}
        trusted_by = {i : 0 for i in range(1, n + 1)}
        
        for i, j in trust:
            trust_to[i] += 1
            trusted_by[j] += 1
        
        for i in range(1, n + 1):
            if trust_to[i] == 0 and trusted_by[i] == n - 1:
                return i
        return -1
