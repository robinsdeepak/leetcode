class Solution:
    def nextGreaterElement(self, n: int) -> int:
        ints = list(map(lambda x: int(x), str(n)))
        n = len(ints)
        
        pivot = n - 2
        found = False
        while (pivot >= 0):
            if (ints[pivot] < ints[pivot + 1]):
                found = True
                break
            pivot -= 1
        
        if not found:
            return -1
        
        swap_idx = pivot + 1
        for j in range(pivot+1, n):
            if (ints[pivot] < ints[j] < ints[swap_idx]):
                swap_idx = j
        
        ints[swap_idx], ints[pivot] = ints[pivot], ints[swap_idx]
        
        ints = ints[:pivot+1] + sorted(ints[pivot+1:])
        # print(ints)
        n2 = int("".join(map(lambda x: str(x), ints)))
        # print(n2)
        return n2 if n2 < 2**31 else -1
    
        