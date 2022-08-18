# from collection import
class Solution:
    def minSetSize(self, arr: List[int]) -> int:
        n = len(arr)
        f = sorted(collections.Counter(arr).items(), key=lambda x: -x[1])
        
        x = 0
        i = 0
        while (x < n / 2) and (i < n):
            x += f[i][1]
            i += 1
        
        return i

        