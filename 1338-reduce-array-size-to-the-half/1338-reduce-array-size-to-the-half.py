class Solution:
    def minSetSize(self, arr: List[int]) -> int:
        n = len(arr)
        counts = sorted(collections.Counter(arr).values(), reverse=True)
        
        x = 0
        i = 0
        while (x < n / 2) and (i < n):
            x += counts[i]
            i += 1
        
        return i
