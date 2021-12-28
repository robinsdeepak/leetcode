class Solution {
public:
    int ans = 0;
    
    void merge(vector<int> &nums, int start, int mid, int end)
    {
        int i = start;
        int j = mid + 1;
        int k = 0;
        
        int len = end - start + 1;
        vector<int> arr(len);
        
        while (i <= mid && j <= end) 
        {
            if (nums[i] < nums[j]) {
                arr[k] = nums[i];
                i++;
            }  else {
                arr[k] = nums[j];
                j++;
            }
            k++;
        }
        
        while (i <= mid) {
            arr[k] = nums[i];
            i++;
            k++;
        }
        
        while (j <= end) {
            arr[k] = nums[j];
            j++;
            k++;
        }
        
        for (i=0; i<len; i++)
        {
            nums[i + start] = arr[i];
        }
        arr.clear();
    }
    
    void mergeSort(vector<int> &nums, int start, int end)
    {
        if (start == end) return;
        
        int mid = start + (end - start) / 2;
        
        mergeSort(nums, start, mid);
        mergeSort(nums, mid + 1, end);
        
        int i = start;
        int j = mid + 1;
        
        for (; i<=mid; i++)
        {
            while (j <= end && (double) nums[i] / 2 > nums[j])
                j++;
            ans += (j - (mid + 1));
        }
        
        merge(nums, start, mid, end);
    }
    
    int reversePairs(vector<int>& nums) 
    {
        int n = nums.size();
        int count = 0;
        mergeSort(nums, 0, nums.size() - 1);

        return ans;
    }
};
