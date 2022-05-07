class Solution:
    def find132pattern(self, nums: List[int]) -> bool:
        n = len(nums)
        st = []
        s3 = None
        
        for i in range(n - 1, -1, -1):
            if s3 is not None and nums[i] < s3:
                return True
            
            while st and st[-1] < nums[i]:
                s3 = st[-1] if s3 is None else max(s3, st[-1])
                st.pop()
            st.append(nums[i])
        
        return False
