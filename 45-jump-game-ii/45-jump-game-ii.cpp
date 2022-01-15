class Solution {
public:
    int jump(vector<int>& nums) 
    {
        int n = nums.size();
        int jumps = 0, max_reach = 0, last_reach = 0, i = 0;
        
        while (last_reach < n - 1)
        {
            max_reach = max(max_reach, i + nums[i]);
            if (i == last_reach)
            {
                jumps++;
                last_reach = max_reach;
            }
            i++;
        }
        return jumps;
    }
};

