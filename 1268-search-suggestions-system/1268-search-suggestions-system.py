import bisect

class Solution:
    def suggestedProducts(self, products: List[str], sw: str) -> List[List[str]]:
        products.sort()
        
        ans, prefix, i = [], '', 0
        
        for c in sw:
            prefix += c
            i = bisect.bisect_left(products, prefix, i)
            ans.append([w for w in products[i:i+3] if w.startswith(prefix)])
            
        return ans
