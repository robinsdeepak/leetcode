class Solution {
public:
    void backtrack(unordered_set<int> indices, vector<int> v, vector<vector<int>> &vv, vector<int>& nums)
    {
        if (indices.size() == nums.size())
        {
            vv.push_back(v);
            return;
        }
        
        for (auto x: nums)
        {
            if (!indices.count(x))
            {
                indices.insert(x);
                v.push_back(x);
                backtrack(indices, v, vv, nums);
                v.pop_back();
                indices.erase(indices.find(x));
            }
        }
    }
    
    vector<vector<int>> permute(vector<int>& nums) 
    {
        vector<int> v;
        vector<vector<int>> vv;
        unordered_set<int> indices;
        
        backtrack(indices, v, vv, nums);
        return vv;
    }
};