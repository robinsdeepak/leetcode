def find(ds, i):
    if ds[i] == i:
        return i
    ds[i] = find(ds, ds[i])
    return ds[i]

class Solution:
    def smallestStringWithSwaps(self, s: str, pairs: List[List[int]]) -> str:
        n = len(s)
        
        ds = [i for i in range(n)]
        
        
        for i, j in pairs:
            r1 = find(ds, i)
            r2 = find(ds, j)
            
            ds[r1] = r2
            
        
        groups = defaultdict(list)
        
        for i in range(n):
            r = find(ds, i)
            groups[r].append(i)
        
        letters = list(s)
        
        for idx in groups.values():
            si = sorted(idx)
            sl = sorted([s[i] for i in si])
            for i, l in zip(si, sl):
                letters[i] = l
        
        return "".join(letters)
