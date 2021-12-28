class Solution {
public:
    int firstMissingPositive(vector<int>& a) 
    {
        int n = a.size();
        
        for (int i=0; i<n; i++)
        {
            while (i < n && a[i] > 0 && a[i] < n && a[i] != a[a[i] - 1])
            { 
                swap(a.at(i), a.at(a[i] - 1));
            }
        }

        int i = 1;
        while (i<=n && i == a[i-1] ) i++;
        return i;
    }
};

