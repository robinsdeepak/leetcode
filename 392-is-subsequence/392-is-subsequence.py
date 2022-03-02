class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        itr = iter(t)
        return all(c in itr for c in s)