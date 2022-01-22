class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        strs2 = sorted([("".join(sorted(strs[i])), i) for i in range(len(strs))], key=lambda x: x[0])
        # print(strs2)
        group = [[strs[strs2[0][1]]]]
        
        for i in range(1, len(strs)):
            if (strs2[i][0] != strs2[i - 1][0]):
                group.append([])
            group[-1].append(strs[strs2[i][1]])

        return group
    