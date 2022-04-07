struct compare {
    bool operator()(int a, int b) {
        return a < b;
    }
};

class Solution {
public:
    int lastStoneWeight(vector<int>& stones) {
        priority_queue<int, vector<int>, compare> pq;
        
        for (int x: stones) {
            pq.push(x);
        }
        
        while (pq.size() > 1) {
            int x = pq.top();
            pq.pop();
            int y = pq.top();
            pq.pop();
            
            if (x != y) {
                pq.push(abs(y - x));
            }
        }
        
        return pq.empty() ? 0 : pq.top();
    }
};
