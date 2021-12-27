class Solution {
public:
    void cs(vector<int>& c, int target, int i, int curr, vector<int> v, vector<vector<int>> &vv)
    {
        if (curr == target)
        {
            vv.push_back(v);
            return;
        }
        if (i == c.size())
            return;
        
        cs(c, target, i + 1, curr, v, vv);
        
        while (curr + c[i] <= target)
        {
            curr += c[i];
            v.push_back(c[i]);

            cs(c, target, i + 1, curr, v, vv);
        }
    }
    
    vector<vector<int>> combinationSum(vector<int>& candidates, int target) 
    {
        vector<int> v;
        vector<vector<int>> vv;
        
        cs(candidates, target, 0, 0, v, vv);
        
        return vv;
    }
};

