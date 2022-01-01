class Solution {
public:

    int candy(vector<int>& arr) 
    {
        int n = arr.size();
        vector<int> candies(n, 1);
        
        for (int i=1; i<n; i++)
        {
            if (arr[i] > arr[i-1])
            {
                candies[i] = candies[i-1] + 1;
            }
        }
        int s = candies[n - 1];
        
        for (int i=n-2; i>=0; i--)
        {
            if (arr[i] > arr[i + 1])
            {
                candies[i] = max(candies[i+1] + 1, candies[i]);
            }
            s += candies[i];
        }
        

        return s;
    }
};