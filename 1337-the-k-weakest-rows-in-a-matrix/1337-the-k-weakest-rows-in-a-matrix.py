class Solution:
    def kWeakestRows(self, mat: List[List[int]], k: int) -> List[int]:
        st = [(sum(mat[i]), i) for i in range(len(mat))]
        
        return sorted(range(len(mat)), key=lambda i: st[i])[:k]
