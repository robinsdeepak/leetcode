class Solution {
public:
    int repeatedStringMatch(string a, string b) 
    {
        string s = "";
        int count = 0;
        while (s.length() < b.length())
        {
            s += a;
            count++;
        }
        
        if (s.find(b) != -1)
            return count;
        
        s += a;
        if (s.find(b) != -1)
            return count + 1;
        
        return -1;
    }
};
