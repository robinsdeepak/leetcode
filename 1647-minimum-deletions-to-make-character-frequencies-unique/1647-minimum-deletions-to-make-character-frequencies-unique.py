from collections import defaultdict
from heapq import *

def get_freq(s):
    freq = defaultdict(int)
    for c in s:
        freq[c] += 1    
    return freq

class Solution:
    def minDeletions(self, s: str) -> int:
        return self.solution_3(s)
    
    def solution_1(self, s):
        
        freq = get_freq(s)        
        cc = sorted(list(freq.items()))
        
        added = set()
        filled = 0
        ans = 0
        
        for char, count in cc:
            for i in range(count, filled, -1):
                if i not in added:
                    added.add(i)
                    ans += (count - i)
                    if i == filled + 1:
                        filled += 1
                    break
            else:
                ans += count
                    
        return ans
    
    def solution_2(self, s):
        freq = get_freq(s)
        
        pq = []
        
        for char, count in freq.items():
            heappush(pq, -count)
        
        ans = 0

        while len(pq) > 1:
            top = -heappop(pq)
            if top == -pq[0]:
                if top > 1:
                    heappush(pq, - (top - 1))
                ans += 1
                
        return ans
    
    def solution_3(self, s):
        freq_dict = get_freq(s)
        frequencies = sorted(list(freq_dict.values()), reverse=True)
        
        max_freq = len(s)
        ans = 0
        
        for freq in frequencies:
            if freq > max_freq:
                ans += (freq - max_freq)
                freq = max_freq
            
            max_freq = max(0, freq - 1)
        
        return ans
