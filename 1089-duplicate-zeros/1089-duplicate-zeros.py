class Solution:
    def duplicateZeros(self, arr: List[int]) -> None:
        """
        Do not return anything, modify arr in-place instead.
        """
        tmp = []
        for x in arr:
            tmp.append(x)
            if (x == 0):
                tmp.append(0)
            if (len(tmp) == len(arr)):
                break
        for i in range(len(arr)):
            arr[i] = tmp[i]
