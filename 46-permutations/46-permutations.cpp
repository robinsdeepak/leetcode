class Solution {
public:
    
    bool find(vector<int> v, int x)
    {
        for (int i: v)
            if (i == x)
                return true;
        return false;
    }
    
    void backtrack(vector<int> v, vector<vector<int>> &vv, vector<int>& nums)
    {
        if (v.size() == nums.size())
        {
            vv.push_back(v);
            return;
        }
        
        for (auto x: nums)
        {
            if (!find(v, x))
            {
                v.push_back(x);
                backtrack(v, vv, nums);
                v.pop_back();
            }
        }
    }
    
    vector<vector<int>> permute(vector<int>& nums) 
    {
        vector<int> v;
        vector<vector<int>> vv;
        
        backtrack(v, vv, nums);
        return vv;
    }
};