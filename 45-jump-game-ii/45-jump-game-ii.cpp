class Solution {
public:
    int solve(vector<int>& dp, vector<int>& nums, int index)
    {
        if (index >= nums.size()-1)
            return 0;
        
        if (dp[index] != -1)
            return dp[index];
        
        int min_jump = nums.size() + 1;
        for (int i=1; i<=nums[index]; i++)
        {
            // cout << index << " " << i + 1 << "/" << nums[index] << " " << min_jump << endl;
            min_jump = min(min_jump, 1 + solve(dp, nums, index + i));
        }
        return dp[index] = min_jump;
    }
    
    int jump(vector<int>& nums) 
    {
        vector<int> dp(nums.size(), -1);
        return solve(dp, nums, 0);
    }
};


