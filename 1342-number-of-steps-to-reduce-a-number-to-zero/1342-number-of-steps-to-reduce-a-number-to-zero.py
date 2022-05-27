class Solution:
    def numberOfSteps(self, num: int) -> int:
        bin_str = bin(num)
        return len(bin_str) + bin_str.count("1") - 3
    