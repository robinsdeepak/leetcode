class Solution:
    def compareVersion(self, version1: str, version2: str) -> int:
        v1 = version1.split(".")
        v2 = version2.split(".")
        m = min(len(v1), len(v2))
        for i in range(m):
            if int(v1[i]) < int(v2[i]):
                return -1;
            elif int(v1[i]) > int(v2[i]):
                return 1
        
        x1 = int("0" + "".join(v1[m:]))
        x2 = int("0" + "".join(v2[m:]))
        
        if (x1 < x2):
            return -1
        if (x1 > x2):
            return 1
        
        return 0
    