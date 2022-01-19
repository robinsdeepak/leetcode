class Solution {
public:
    bool canPlaceFlowers(vector<int>& flowerbed, int req) 
    {
        int n = flowerbed.size();
        int count = 0;
        
        if (n == 1)
        {
            count = flowerbed[0] == 0 ? 1 : 0;
            return req <= count;
        }
        
        if (flowerbed[0] == 0 && flowerbed[1] == 0)
        {
            count++;
            flowerbed[0] = 1;
        }
        
        if (flowerbed[n - 1] == 0 && flowerbed[n - 2] == 0)
        {
            count++;
            flowerbed[n-1] = 1;
        }
        
        for (int i=1; i<n-1; i++)
        {
            if (flowerbed[i-1] == 0 && flowerbed[i] == 0 && flowerbed[i+1] == 0)
            {
                count++;
                flowerbed[i] = 1;
            }
        }
        return req <= count;
    }
};

