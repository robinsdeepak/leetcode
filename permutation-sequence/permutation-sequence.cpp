class Solution 
{
public:
    unordered_map<int,int> factorials;
    
    void calculate_factorials()
    {
        factorials[0] = 1;
        for (int i=1; i<=9; i++)
        {
            factorials[i] = factorials[i - 1] * i;
        }
    }
    
    string getPermutation(int n, int k) 
    {
        calculate_factorials();
        vector<int> numbers;
        
        for (int i=1; i<=n; i++)
            numbers.push_back(i);
        
        k = k - 1;
        
        string ans = "";
        
        while (numbers.size())
        {
            int fact = factorials[numbers.size() - 1];
            int index = k / fact;
            ans += to_string(numbers[index]);
            numbers.erase(numbers.begin() + index);
            k %= fact;
        }
        return ans;
    }
};

