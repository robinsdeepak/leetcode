class Solution {
public:
    
    string lcp(string s1, string s2)
    {
        string cp = "";
        for (int i=0; i < min(s1.length(), s2.length()); i++)
        {
            if (s1[i] == s2[i]) {
                cp += s1[i];
            } else {
                return cp;
            }
        }
        return cp;
    }
    
    string longestCommonPrefix(vector<string>& strs) {
        string cp = strs[0];
        
        for (int i=1; i<strs.size(); i++)
        {
            cp = lcp(cp, strs[i]);
        }
        return cp;
    }
};