class Solution:
    def isPossible(self, nums: List[int]) -> bool:
        seq = defaultdict(int)
        freq = collections.Counter(nums)
        
        for n in nums:
            if not freq[n]:
                continue
            
            if seq[n - 1] > 0:
                seq[n - 1] -= 1
                seq[n] += 1
                freq[n] -= 1
            
            else:
                if not freq[n + 1] or not freq[n + 2]:
                    return False
                
                freq[n] -= 1
                freq[n + 1] -= 1
                freq[n + 2] -= 1
                seq[n + 2] += 1
            
        
        return True
