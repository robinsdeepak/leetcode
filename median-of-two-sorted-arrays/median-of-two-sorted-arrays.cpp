class Solution {
public:
    double findMedianSortedArrays(vector<int>& nums1, vector<int>& nums2) {
        int N1 = nums1.size();
        int N2 = nums2.size();
        if (N1 > N2) return findMedianSortedArrays(nums2, nums1);	// Make sure A1 is the shorter one.

        int lo = 0, hi = N1 * 2;
        while (lo <= hi) {
            int mid1 = (lo + hi) / 2;
            int mid2 = N1 + N2 - mid1;

            int L1 = (mid1 == 0) ? INT_MIN : nums1[(mid1-1)/2];
            int L2 = (mid2 == 0) ? INT_MIN : nums2[(mid2-1)/2];
            int R1 = (mid1 == N1 * 2) ? INT_MAX : nums1[(mid1)/2];
            int R2 = (mid2 == N2 * 2) ? INT_MAX : nums2[(mid2)/2];

            if (L1 > R2) hi = mid1 - 1;		// A1's lower half is too big; need to move left of A1
            else if (L2 > R1) lo = mid1 + 1;	// A2's lower half too big; need to move left of A2
            else return (max(L1,L2) + min(R1, R2))/2.0;	// Otherwise, that's the right cut.
        }
        return -1;
    }
};