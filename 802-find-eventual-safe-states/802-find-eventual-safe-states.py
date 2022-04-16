class Solution:
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        n = len(graph)
        sn = {}
        for i in range(n):
            if len(graph[i]) == 0:
                sn[i] = True
        
        flag = True
        
        while flag:
            flag = False           
            for i in range(n):
                if i in sn: 
                    continue
                for j in graph[i]:
                    if not sn.get(j):
                        break
                else:
                    sn[i] = True
                    flag = True

        return sorted(list(sn))
