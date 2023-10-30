class Solution:
    def sortByBits(self, arr: List[int]) -> List[int]:
        return self.solution_2(arr)
    
    def solution_1(self, arr):
        
        arr.sort(key=lambda x: (n.bit_count(), n))
        
        return arr
    
    def solution_2(self, arr):
        def find_weight(num):
            weight = 0
            
            while num:
                weight += 1
                num &= (num - 1)
            
            return weight
        
        arr.sort(key = lambda num: (find_weight(num), num))
        return arr
