class Solution {
public:
    void cs(vector<vector<int>> cd, int t, vector<int> v, vector<vector<int>> &vv, int i, int curr)
    {
        if (curr == t)
        {
            vv.push_back(v);
            return;
        }
        if (i == cd.size() || curr > t) return;
        
        cs(cd, t, v, vv, i + 1, curr);
        
        for (int j=0; j<cd[i][1] && curr <= t; j++)
        {
            curr += cd[i][0];
            v.push_back(cd[i][0]);
            cs(cd, t, v, vv, i + 1, curr);
        }
    }
    
    vector<vector<int>> combinationSum2(vector<int>& candidates, int target) 
    {
        map<int,int> m;
        for (auto x: candidates) m[x]++;
        
        vector<vector<int>> cd;
        
        for (auto it: m) cd.push_back({it.first, it.second});
        
        vector<int> v;
        vector<vector<int>> vv;
        cs(cd, target, v, vv, 0, 0);
        
        return vv;
    }
};