class Solution:
    
    def countSmaller(self, nums: List[int]) -> List[int]:
        n = len(nums)
        v = list(enumerate(nums))
        count = [0] * n
        
        def merge(s, m, e):
            i, j, k = s, m + 1, 0
            aux = [0] * (e - s + 1)
            
            while i <= m and j <= e:
                if v[i][1] > v[j][1]:
                    count[v[i][0]] += (e - j + 1)
                    aux[k] = v[i]
                    i += 1
                else:
                    aux[k] = v[j]
                    j += 1
                k += 1
            
            while i <= m:
                aux[k] = v[i]
                i += 1
                k += 1

            while j <= e:
                aux[k] = v[j]
                j += 1
                k += 1
                
            v[s: e + 1] = aux
        
        def mergeSort(s, e):
            if s == e:
                return
            
            m = (s + e) // 2
            
            mergeSort(s, m)
            mergeSort(m + 1, e)
            
            merge(s, m, e)
        
        mergeSort(0, n - 1)
        
        return count
