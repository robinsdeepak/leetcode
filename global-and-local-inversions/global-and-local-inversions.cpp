class Solution {
public:
    int g_inv = 0;
    int l_inv = 0;

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
    
    bool mergeSort(vector<int> &nums, int start, int end)
    {
        if (start == end) return true;
        
        int mid = start + (end - start) / 2;
        
        if (!mergeSort(nums, start, mid) || !mergeSort(nums, mid + 1, end))
            return false;
        
        
        int i = start;
        int j = mid + 1;
        
        for (; i<=mid; i++)
        {
            while (j <= end && nums[i] > nums[j])
                j++;
            g_inv += (j - (mid + 1));
            if (g_inv > l_inv) return false;
        }
        
        merge(nums, start, mid, end);
        return true;
    }

    bool isIdealPermutation(vector<int>& nums) 
    {
        int n = nums.size();
        
        for (int i=0; i<n-1; i++)
            l_inv += (nums[i] > nums[i+1]);
        
        return mergeSort(nums, 0, nums.size() - 1);
        
        // return l_inv == g_inv;
    }
};