class Trie
{

private:
    struct TrieNode 
    {
        bool isEnd = false;
        TrieNode *childs[26];
    };
    TrieNode *node;
    
public:
    Trie()
    {
        node = new TrieNode();
    }

    void insert(string word)
    {
        TrieNode *curr = node;
        for (char c: word)
        {
            if (curr->childs[c - 'a'] == NULL)
                curr->childs[c - 'a'] = new TrieNode();
            curr = curr->childs[c - 'a'];
        }
        curr->isEnd = true;
    }

    bool search(string word)
    {
        TrieNode *curr = node;
        for (char c: word)
        {
            if (curr->childs[c - 'a'] == NULL)
                return false;
            curr = curr->childs[c - 'a'];
        }
        return curr->isEnd;
    }

    bool startsWith(string prefix)
    {
        TrieNode *curr = node;
        for (char c: prefix)
        {
            if (curr->childs[c - 'a'] == NULL)
                return false;
            curr = curr->childs[c - 'a'];
        }
        return true;
    }
};