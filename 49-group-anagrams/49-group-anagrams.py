class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        str_dict = {}
        for s in strs:
            ss = "".join(sorted(s))
            if ss not in str_dict:
                str_dict[ss] = []
            str_dict[ss].append(s)
        return list(str_dict.values())
    
    
    