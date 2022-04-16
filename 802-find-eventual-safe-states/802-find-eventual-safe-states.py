class Solution:
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        n = len(graph)
        sn = set()
        for i in range(n):
            if len(graph[i]) == 0:
                sn.add(i)
        
        flag = True
        
        while flag:
            flag = False           
            for i in range(n):
                if i in sn: 
                    continue
                for j in graph[i]:
                    if j not in sn:
                        break
                else:
                    sn.add(i)
                    flag = True

        return sorted(list(sn))
