class Solution {
public:
    bool wordBreak(string s, vector<string>& wordDict) 
    {
        vector<bool> res(s.size() + 1, false);
        int n = s.size();
        
        res[n] = true;
        
        for (int i=n - 1; i >= 0; i--)
        {
            for (string w: wordDict)
            {
                if (w.size() <= n - i && res[i + w.size()] && 
                    (w == s.substr(i, w.size())))
                {
                    res[i] = true;
                    break;
                }
            }
        }
        return res[0];
    }
};