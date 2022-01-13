class Solution {
public:
    vector<int> maxSlidingWindow(vector<int>& nums, int k) 
    {        
        if (k == 1) return nums;
        vector<int> mv;
   
        deque<int> dq;
        
        for (int i=0; i<nums.size(); i++)
        {
            while (!dq.empty() && dq.front() < i - k + 1)
            {
                dq.pop_front();
            }
            while (!dq.empty() && nums[dq.back()] <= nums[i])
            {
                dq.pop_back();
            }
            dq.push_back(i);
            if (i >= k-1) mv.push_back(nums[dq.front()]);
        }
            
        return mv;
    }
};

