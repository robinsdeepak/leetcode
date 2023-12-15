class Solution:
    def destCity(self, paths: List[List[str]]) -> str:
        src = {s for s, d in paths}
        # print(src)
        for s, d in paths:
            if d not in src:
                return d
        return -1
