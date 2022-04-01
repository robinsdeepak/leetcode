def check(arr, max_sum, sub_arr_count):
    count = 1
    curr = 0
    
    for x in arr:
        if curr + x <= max_sum:
            curr += x
        else:
            curr = x
            count += 1
        
        if count > sub_arr_count:
            return False
    
    return count <= sub_arr_count
    

class Solution:
    def splitArray(self, nums: List[int], m: int) -> int:
        n = len(nums)
        high = sum(nums)
        low = max(nums)
        
        ans = high
        
        while (low <= high):
            mid = (low + high) // 2
            
            if (check(nums, mid, m)):
                ans = min(ans, mid)
                high = mid - 1
            else:
                low = mid + 1
        
        return ans
