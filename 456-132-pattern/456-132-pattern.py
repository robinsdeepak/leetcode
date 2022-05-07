class Solution:
    def find132pattern(self, nums: List[int]) -> bool:
        n = len(nums)
        st = []
        s3 = float('-inf')
        
        for i in range(n - 1, -1, -1):
            if nums[i] < s3:
                return True
            
            while st and st[-1] < nums[i]:
                s3 = max(s3, st[-1])
                st.pop()
            st.append(nums[i])
        
        return False
