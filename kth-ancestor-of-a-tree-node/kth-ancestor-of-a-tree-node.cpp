auto speedup = []() {
    std::ios::sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);
    return 0;
}();


class TreeAncestor {
public:
    vector<vector<int>> up;
    int logn=1;
    
    TreeAncestor(int n, vector<int>& parent) {
        up = vector<vector<int>> (n, vector<int>(20, -1));
        
        while ((1 << logn) <= n) logn++;
        
        for (int i=0; i<n; i++)
        {
            up[i][0] = parent[i];
        }
        
        for (int i=0; i<n; i++)
        {
            for (int j=1; j<logn; j++)
            {
                int p = up[i][j - 1];
                if (p == -1) break;
                up[i][j] = up[p][j-1];
            }
        }
    }
    
    int getKthAncestor(int node, int k) {

        for (int i=0; i<logn; i++)
        {
            if (k & (1 << i))
            {
                node = up[node][i];
                if (node == -1) break;
            }
        }
        return node;
    }
};

/**
 * Your TreeAncestor object will be instantiated and called as such:
 * TreeAncestor* obj = new TreeAncestor(n, parent);
 * int param_1 = obj->getKthAncestor(node,k);
 */