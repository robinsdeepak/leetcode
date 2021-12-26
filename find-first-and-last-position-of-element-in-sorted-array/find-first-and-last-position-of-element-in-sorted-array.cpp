class Solution {
public:
    vector<int> searchRange(vector<int>& nums, int target) {
        
        int n = nums.size();
        int l = 0;
        int h = n - 1;
        int mid;
        
        vector<int> range(2, -1);
        int e = -1;
        
        while (l <= h) {
            mid = (l + h) / 2;
            if (nums[mid] == target) {
                e = max(e, mid);
                if (mid == 0 || nums[mid-1] < target) {
                    range[0] = mid;
                    break;                    
                } else {
                    h = mid - 1;
                    continue;
                }
            }
            
            if (nums[mid] < target) {
                l = mid + 1;
            } else {
                h = mid - 1;
            }
        }
        
        l = e ? e > 0: 0;
        h = n - 1;
        // cout << e << endl;
        
        while (l <= h) {
            mid = (l + h) / 2;
            
            if (nums[mid] == target) {
                if (mid == n - 1 || nums[mid+1] > target) {
                    range[1] = mid;
                    break;                    
                } else {
                    l = mid + 1;
                    continue;
                }
            }
            
            if (nums[mid] > target) {
                h = mid - 1;
            } else {
                l = mid + 1;
            }
        }
        return range;
    }
};