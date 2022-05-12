class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        ans = []
        def rec(idx, path):
            if not idx:
                ans.append(path)
            
            for i in idx:
                tmp = idx.copy()
                tmp.remove(i)
                rec(tmp, path + [nums[i]])
        
        rec(set(range(len(nums))), [])
        return ans

    