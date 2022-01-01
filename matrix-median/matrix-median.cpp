
int Solution::findMedian(vector<vector<int>> &A) 
{
    int n1 = A.size();
    int n2 = A[0].size();
    
    int min_ = INT_MAX;
    int max_ = INT_MIN;
    for (int i=0; i<n1; i++)
    {
        for (int j=0; j<n2; j++)
        {
            min_ = min(min_, A[i][j]);
            max_ = max(max_, A[i][j]);
        }
    }

    int l = min_;
    int h = max_;

    while (l < h)
    {
        int mid = l + (h - l) / 2;
        int count = 0;
        for (int i=0; i<n1; i++)
        {
            count = count + upper_bound(A[i].begin(), A[i].end(), mid)- A[i].begin();
        }
        
        if(count< ((n1 * n2 + 1) / 2))
            l = mid + 1;
        else
            h = mid;
    }
    return l;
}

