class Solution:
    def suggestedProducts(self, products: List[str], searchWord: str) -> List[List[str]]:
        
        m = {}
        
        for i, pd in enumerate(products):
            for j in range(len(pd)):
                pref = pd[:j + 1]
                
                if not searchWord.startswith(pref):
                    break
                
                if pref not in m:
                    m[pref] = []
                
                m[pref].append(i)
                
                if len(m[pref]) == 4:
                    m[pref].remove(max(m[pref], key=lambda x: products[x]))
        
        ans = []
        for j in range(len(searchWord)):
            pref = searchWord[:j + 1]
            ans.append(sorted(list(map(lambda x: products[x], m.get(pref, [])))))
        
        return ans
