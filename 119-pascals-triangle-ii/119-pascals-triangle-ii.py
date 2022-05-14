class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        l1 = []
        for i in range(rowIndex + 1):
            l2 = [1] * (i + 1)
            
            for j in range(1, i):
                l2[j] = l1[j-1] + l1[j]
            l1 = l2
            
        return l1
