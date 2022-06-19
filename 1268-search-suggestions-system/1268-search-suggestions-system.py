class Solution:
    def suggestedProducts(self, products: List[str], searchWord: str) -> List[List[str]]:
        
        m = {}
        
        for i, pd in enumerate(products):
            for j in range(1, len(pd) + 1):
                pref = pd[:j]
                
                if pref not in m:
                    m[pref] = []
                
                m[pref].append(i)
                
                if len(m[pref]) == 4:
                    m[pref].remove(max(m[pref], key=lambda x: products[x]))
        
        ans = []
        for j in range(1, len(searchWord) + 1):
            pref = searchWord[:j]
            ans.append(sorted(list(map(lambda x: products[x], m.get(pref, [])))))
        
        return ans
