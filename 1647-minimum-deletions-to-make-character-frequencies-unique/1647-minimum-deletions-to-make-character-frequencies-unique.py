from collections import defaultdict

class Solution:
    def minDeletions(self, s: str) -> int:
        freq = defaultdict(int)
        for c in s:
            freq[c] += 1
        
        cc = sorted(list(freq.items()))
        
        added = set()
        filled = 0
        ans = 0
        
        # print(cc)
        
        for char, count in cc:
            for i in range(count, filled, -1):
                if i not in added:
                    added.add(i)
                    ans += (count - i)
                    # print(char, count, i)
                    if i == filled + 1:
                        filled += 1
                    break
            else:
                ans += count
                    
        return ans
