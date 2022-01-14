class Solution {
public:
    
    void backtrack(vector<vector<int>> &vv, unordered_map<int,int> &freq, vector<int> curr, vector<int>& nums)
    {
        if (curr.size() == nums.size())
        {
            vv.push_back(curr);
            return;
        }
        
        for (auto it: freq)
        {
            int n = it.first;
            
            if (count(curr.begin(), curr.end(), n) < it.second)
            {
                curr.push_back(n);
                backtrack(vv, freq, curr, nums);
                curr.pop_back();
            }
        }
    }
    
    vector<vector<int>> permuteUnique(vector<int>& nums) 
    {
        unordered_map<int,int> freq;
        for (int n: nums) freq[n]++;
        vector<vector<int>> vv;
        vector<int> v;
        backtrack(vv, freq, v, nums);

        return vv;
    }
};



