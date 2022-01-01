
bool isSafe(bool graph[101][101], int m, vector<int> &colors, int vi, int ci)
{
    int n = colors.size();
    for (int i=0; i < n; i++)
    {
        if (graph[vi][i] == 1)
        {
            if (colors[i] == ci)
                return false;
        }
    }
    return true;
}

bool solve(bool graph[101][101], int m, vector<int> &colors, int vi)
{
    // all the vertices have been colored safely
    if (vi >= colors.size()) return true;
    
    // check for all colors if safe for the current vertex
    for (int i=0; i<m; i++)
    {
        if (isSafe(graph, m, colors, vi, i))
        {
            colors[vi] = i;
            if(solve(graph, m, colors, vi + 1))
                return true;
            else
                colors[vi] = -1;
        }
    }
    return false;
}

bool graphColoring(bool graph[101][101], int m, int V)
{
    vector<int> colors(V, -1);
    return solve(graph, m, colors, 0);
}
