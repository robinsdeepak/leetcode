class NumArray:

    def __init__(self, nums: List[int]):
        self.nums = nums
        self.n = len(nums)
        self.sn = math.ceil(math.sqrt(self.n))
        self.bs = [0] * self.sn
        
        for i in range(self.n):
            self.bs[i // self.sn] += nums[i]
        

    def update(self, index: int, val: int) -> None:
        bi = index // self.sn
        self.bs[bi] += (val - self.nums[index])
        self.nums[index] = val

    def sumRange(self, left: int, right: int) -> int:
        ans = 0
        sb = left // self.sn
        eb = right // self.sn
        
        if (sb == eb):
            for i in range(left, right + 1):
                ans += self.nums[i]
        else:
            for i in range(left, (sb + 1) * self.sn):
                ans += self.nums[i]
            
            for i in range(sb + 1, eb):
                ans += self.bs[i]
            
            for i in range(eb * self.sn, right + 1):
                ans += self.nums[i]
        return ans

# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# obj.update(index,val)
# param_2 = obj.sumRange(left,right)
