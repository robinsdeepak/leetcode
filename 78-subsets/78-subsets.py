class Solution:
  
    def subsets(self, nums: List[int]) -> List[List[int]]:
        return reduce((lambda ls, x: ls + list(map(lambda y: y+[x], ls))), nums, [[]])