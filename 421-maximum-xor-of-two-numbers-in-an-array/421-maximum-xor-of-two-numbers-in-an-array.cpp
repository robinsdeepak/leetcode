class Solution {
public:
    int findMaximumXOR(vector<int>& nums) 
    {
        int mask = 0, mx = 0;
        for (int i=31; i>=0; i--)
        {
            mask = mask | (1 << i);
            unordered_set<int> s;
            
            for (int x: nums)
                s.insert(x & mask);
            
            for (int x: s)
            {
                if (s.count(x ^ (mx | (1 << i))))
                {
                    mx = mx | (1 << i);
                    break;
                }
            }
        }
        return mx;
    }
};
