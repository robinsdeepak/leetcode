bool isClose(int target, int old, int new_)
{
    return abs(target - old) > abs(target - new_);
}

class Solution {
public:
    int threeSumClosest(vector<int>& nums, int target) 
    {  
        if(nums.size() < 3) return 0;
        int closest_sum = nums[0]+nums[1]+nums[2];        
        
        sort(nums.begin(), nums.end());
        int n = nums.size();
        int i=0, j, k = n - 1;
        
        while (i < k)
        {
            j = i + 1;
            k = n - 1;
            while (j < k)
            {
                int curr_sum = nums[i] + nums[j] + nums[k];
                
                if (curr_sum == target)
                    return target;
                
                if (isClose(target, closest_sum, curr_sum))
                    closest_sum = curr_sum;
                
                if (curr_sum < target)
                    j++;
                else
                    k--;
            }
            i++;
        }
        return closest_sum;
    }
};
