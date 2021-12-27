class Solution {
public:
    
    void  ss(vector<vector<int>> nm, vector<int> v, vector<vector<int>> &vv, int i)
    {
        if (i == nm.size())
        {
            vv.push_back(v);
            return;
        }
        
        ss(nm, v, vv, i + 1);
        for (int j=0; j<nm[i][1]; j++)
        {
            v.push_back(nm[i][0]);            
            ss(nm, v, vv, i + 1);
        }
    }
    
    vector<vector<int>> subsetsWithDup(vector<int>& nums) 
    {
        map<int,int> m;
        
        for (auto x: nums) m[x]++;
        vector<vector<int>> nm;
        
        for (auto it: m) nm.push_back({it.first, it.second});
        
        vector<vector<int>> vv;
        vector<int> v;
        ss(nm, v, vv, 0);
        return vv;
    }
};


