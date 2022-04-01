class Solution:
    def splitArray(self, nums: List[int], m: int) -> int:
        n = len(nums)
        prefix = [0]
        for x in nums: prefix.append(prefix[-1] + x)
        
        @functools.lru_cache(None)
        def solve(idx, scount):
            if scount == 1:
                return prefix[-1] - prefix[idx]
        
            mlss = prefix[-1]
            for i in range(idx, n - scount + 1):
                first_split_sum = prefix[i + 1] - prefix[idx]
                largest_split_sum = max(first_split_sum, solve(i + 1, scount - 1))
                mlss = min(mlss, largest_split_sum)

                if first_split_sum >= mlss:
                    break
            
            return mlss
            
        return solve(0, m)
