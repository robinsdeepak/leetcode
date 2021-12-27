class Solution {
public:
    
    void  ss(vector<int>& nums, vector<int> v, vector<vector<int>> &vv, int i)
    {
        if (i == nums.size())
        {
            vv.push_back(v);
            return;
        }
        
        ss(nums, v, vv, i + 1);
        v.push_back(nums[i]);
        ss(nums, v, vv, i + 1);
    }
    
    vector<vector<int>> subsets(vector<int>& nums) 
    {
        vector<vector<int>> vv;
        vector<int> v;
        ss(nums, v, vv, 0);
        return vv;
    }
};
