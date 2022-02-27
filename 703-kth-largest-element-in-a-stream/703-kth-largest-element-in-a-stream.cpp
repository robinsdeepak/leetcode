class KthLargest {
public:
    multiset<int, greater<int>> s1;
    multiset<int, greater<int>> s2;
    int K;
    
    KthLargest(int k, vector<int>& nums) {
        s1.clear();
        s2.clear();
        K = k;
        for (int x: nums) add(x);
    }
    
    int add(int val) {
        s1.insert(val);
        
        if (s1.size() > K) {
            int last = *s1.rbegin();
            s1.erase(prev(s1.end()));
            s2.insert(last);
        }
        
        return (*s1.rbegin());
    }
};

/**
 * Your KthLargest object will be instantiated and called as such:
 * KthLargest* obj = new KthLargest(k, nums);
 * int param_1 = obj->add(val);
 */