class Solution:
    def suggestedProducts(self, products: List[str], sw: str) -> List[List[str]]:
        
        ans = [[] for _ in sw]
        
        for pd in products:
            for j in range(min(len(pd), len(sw))):
                if pd[j] != sw[j]:
                    break
                
                if len(ans[j]) < 3:
                    ans[j].append(pd)
                    
                elif pd < ans[j][2]:
                    ans[j][2] = pd
                    
                ans[j].sort()
                
        return ans
