class Solution {
public:
    int Min(int a, int b, int c)
    {
        return min(min(a, b), c);
    }

    int minDistance(string word1, string word2) 
    {
        int l1 = word1.length();
        int l2 = word2.length() ;
        
        vector<vector<int>> memo(l1 + 1, vector<int>(l2 + 1, 0));
        for (int i=0;i<=l1;i++) memo[i][0]=i;
        for (int j=0;j<=l2;j++) memo[0][j]=j;
        
        int ss;
        
        for (int i=1; i<=l1; i++)
        {
            for (int j=1; j<=l2; j++)
            {
                ss = (word1[i-1] == word2[j-1]) ? 0 : 1;
                memo[i][j] = Min(memo[i - 1][j] + 1, memo[i][j - 1] + 1, memo[i - 1][j - 1] + ss);
            }
        }

        return memo[l1][l2];
    }
};