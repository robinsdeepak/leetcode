class Solution {
public:
    int minimumDeviation(vector<int>& nums) 
    {
        int diff = INT_MAX, min_n = INT_MAX;
        set<int> s;
        
        for (int x: nums)
        {
            x = (x % 2) ? x * 2 : x;
            s.insert(x);
            min_n = min(min_n, x);
        }
        
        
        while ((*(s.rbegin())) % 2 == 0)
        {
            int top = *(s.rbegin());
            diff = min(diff, top - min_n);
            min_n = min(min_n, top / 2);
            s.erase(top);
            s.insert(top / 2);
        }
        return min(diff, (*(s.rbegin())) - min_n); 
    }
};
