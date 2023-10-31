class Solution:
    def findArray(self, pref: List[int]) -> List[int]:
        n = len(pref)
        arr =  [pref[i - 1] ^ pref[i] for i in range(n)]
        arr[0] = pref[0]
        return arr
