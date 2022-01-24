class Solution:
    def next_seq(self, seq: str):
        n = seq[0]
        c = 0
        result = ""
        
        for i in range(len(seq)):
            if seq[i] == n:
                c += 1
            else:
                result = result + str(c) + n
                n = seq[i]
                c = 1
        result = result + str(c) + n
        return result
    
    def countAndSay(self, n: int) -> str:
        res = "1"
        for i in range(n-1):
            res = self.next_seq(res)
        return res
    