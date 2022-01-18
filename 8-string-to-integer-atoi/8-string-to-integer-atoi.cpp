class Solution {
public:
    int myAtoi(string s) {
        int n = 0;
        int m = 10;
        int sign = 1;
        int lead = true;
        for (char c: s) {
            if (c == ' ' && lead) {
                continue;
            }
            else if (c == '-' && lead) {
                if (!lead) return 0;
                sign = -1;
                lead = false;
            }
            else if (c == '+' && lead)
            {
                if (!lead) return 0;
                lead = false;
            }
            else if (c >= '0' && c <= '9') {
                lead = false;
                int x = c - '0';
                if (n > INT_MAX / 10 || (n == INT_MAX / 10 && x * sign > 7)) 
                    return INT_MAX;
                if (n < INT_MIN / 10 || (n == INT_MIN / 10 && x * sign < -8)) 
                    return INT_MIN;
                n = (n * m) + (c - '0') * sign;
            }
            else
                return n;
        }
        return n;
    }
};