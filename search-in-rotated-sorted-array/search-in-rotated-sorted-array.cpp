class Solution {
public:
    int search(vector<int>& nums, int target) {
        int n = nums.size();
        int l = 0, h = n - 1;
        int m;
        
        while (l <= h) {
            m = (l + h) / 2;
            
            if (target == nums[m])
                return m;
            
            if (nums[m] >= nums[l]) {
                if (target >= nums[l] && target < nums[m])
                    h = m - 1;
                else
                    l = m + 1;
            } else {
                if (target > nums[m] && target <= nums[h])
                    l = m + 1;
                else
                    h = m - 1;
            }
        }
        return -1;
    }
};