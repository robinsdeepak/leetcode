class Solution {
public:
    bool searchMatrix(vector<vector<int>>& matrix, int target) {
        long long int row = matrix.size();
        long long int col = matrix[0].size();
        
        long long int low = 0;
        long long int high = row * col - 1;
        long long int mid;
        
        long long int r, c;
        
        while (low <= high)
        {
            mid = ( low + high ) / 2;
            r = mid / col;
            c = mid % col;
            
            if (matrix[r][c] == target)
            {
                return true;
            }
            else if (matrix[r][c] < target)
            {
                low = mid + 1;
            }
            else 
            {
                high = mid - 1;
            }
        }
        return false;
    }
};