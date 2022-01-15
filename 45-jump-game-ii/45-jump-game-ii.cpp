class Solution {
public:
    int solve(vector<int>& dp, vector<int>& nums, int index)
    {
        if (index >= nums.size()-1)
            return 0;
        
        if (dp[index] != nums.size() + 1)
            return dp[index];
        
        for (int i=1; i<=nums[index]; i++)
        {
            dp[index] = min(dp[index], 1 + solve(dp, nums, index + i));
        }
        return dp[index];
    }
    
    int jump(vector<int>& nums) 
    {
        vector<int> dp(nums.size(), nums.size() + 1);
        return solve(dp, nums, 0);
    }
};


