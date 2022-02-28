class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        if not nums:
            return []
        
        ranges = []
        curr = [0, 0]
        for i in range(1, len(nums)):
            if nums[i] != nums[curr[-1]] + 1:
                ranges.append(curr.copy())
                curr = [i, i]
            else:
                curr[-1] += 1
        
        if (not ranges or ranges[-1][-1] != curr[-1]):
            ranges.append(curr)
        
        out = ["->".join(map(lambda x: str(nums[x]), set(r))) for r in ranges]
        return out
