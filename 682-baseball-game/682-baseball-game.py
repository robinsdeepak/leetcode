class Solution:
    def calPoints(self, ops: List[str]) -> int:
        arr = []
        for x in ops:
            if x == "+":
                arr.append(arr[-1] + arr[-2])
            elif x == "D":
                arr.append(arr[-1] * 2)
            elif x == "C":
                arr.pop()
            else:
                arr.append(int(x))
        
        return sum(arr)
