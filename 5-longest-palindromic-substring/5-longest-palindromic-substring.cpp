class Solution {
public:
    string longestPalindrome(string s) 
    {
        int n = s.length();
        int dp[n][n];
        
        int start=0, len=1, max_len=1;
        
        for (int i=0; i<n; i++)
        {
            for (int j=0; j<n; j++)
            {
                dp[i][j] = 0;
            }
        }
        
        for (int i=0; i<n; i++)
            dp[i][i] = 1;
        
        for (int i=0; i<n-1; i++)
        {
            if (s[i] == s[i+1])
            {
                dp[i][i+1] = 1;
                max_len = 2;
                start = i;
            }
        }
        
        
        for (int l=3; l<=n; l++)
        {
            for (int i=0; i<=n-l; i++)
            {
                if (s[i] == s[i+l-1] && dp[i+1][i+l-2]==1)
                {
                    dp[i][i+l-1]=1;
                    
                    if (max_len<l) {
                        max_len = l;
                        start = i;
                    }
                }
            }
        }
        
        return s.substr(start, max_len);
    }
};
