class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        k %= n
        
        def rev(s, e, a):
            while s < e:
                a[s], a[e] = a[e], a[s]
                s += 1
                e -= 1
        
        rev(0, n - 1, nums)
        rev(0, k - 1, nums)
        rev(k, n - 1, nums)
    
        