class Solution:
    def hasAllCodes(self, s: str, k: int) -> bool:
        # if (len(s) - k + 1) < (1 << k):
        #     return False
        
        bins = set()
        for i in range(k, len(s) + 1):
            # print(i)
            bins.add(s[i - k : i])
            
            if (len(bins) + len(s) - i) < (1 << k):
                return False
            # print((len(bins) + len(s) - i), (1 << k))
            
        return len(bins) == 1 << k
