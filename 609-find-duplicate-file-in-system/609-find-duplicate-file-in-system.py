class Solution:
    def findDuplicate(self, paths: List[str]) -> List[List[str]]:
        m = defaultdict(list)
        
        for p in paths:
            tokens = p.split()
            d = tokens[0]
            
            for fc in tokens[1:]:
                s = fc.find('(')
                e = fc.rfind(')')
                f = fc[:s]
                c = fc[s + 1: e]
                # print(fc, f, c)    
                
                m[c].append(d + '/' + f)
        # print(m)
        return [v for k, v in m.items() if len(v) > 1]
