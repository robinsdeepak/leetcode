// The API isBadVersion is defined for you.
// bool isBadVersion(int version);

class Solution {
public:
    int firstBadVersion(int n) {
        long long int low=1, high=n, mid;
        while (low <= high) {
            mid = (low + high) / 2;
            
            if (isBadVersion(mid)) {
                if (!isBadVersion(mid-1)) {
                    return mid;
                } else {
                    high = mid - 1;                    
                }
            } else {
                low = mid + 1;
            }
        }
        return -1;
    }
};
