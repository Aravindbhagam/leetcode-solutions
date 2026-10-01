#include <limits.h>

double findMedianSortedArrays(int* nums1, int m, int* nums2, int n) {
    if (m > n)
        return findMedianSortedArrays(nums2, n, nums1, m);

    int low = 0, high = m;
    int half = (m + n + 1) / 2;

    while (low <= high) {
        int cut1 = (low + high) / 2;
        int cut2 = half - cut1;

        int left1  = (cut1 == 0) ? INT_MIN : nums1[cut1 - 1];
        int right1 = (cut1 == m) ? INT_MAX : nums1[cut1];

        int left2  = (cut2 == 0) ? INT_MIN : nums2[cut2 - 1];
        int right2 = (cut2 == n) ? INT_MAX : nums2[cut2];

        if (left1 <= right2 && left2 <= right1) {
            // Correct partition found
            if ((m + n) % 2 == 0) {
                int maxLeft = left1 > left2 ? left1 : left2;
                int minRight = right1 < right2 ? right1 : right2;
                return (maxLeft + minRight) / 2.0;
            } else {
                return (left1 > left2 ? left1 : left2);
            }
        }
        else if (left1 > right2) {
            high = cut1 - 1;
        }
        else {
            low = cut1 + 1;
        }
    }
    return 0.0;
}

