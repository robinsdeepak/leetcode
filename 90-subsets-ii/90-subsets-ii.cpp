class Solution {
public:
    
    void  ss(vector<int>& nums, vector<int> v, vector<vector<int>> &vv, int i)
    {
        vv.push_back(v);
        
        for (int j = i; j < nums.size(); j++) 
        {
            if (j == i || nums[j] != nums[j - 1])
            {
                v.push_back(nums[j]);
                ss(nums, v, vv, j + 1);
                v.pop_back();   
            }
		}
    }
    
    vector<vector<int>> subsetsWithDup(vector<int>& nums) 
    {   
        sort(nums.begin(), nums.end());
        vector<vector<int>> vv;
        vector<int> v;
        ss(nums, v, vv, 0);
        return vv;
    }
};


