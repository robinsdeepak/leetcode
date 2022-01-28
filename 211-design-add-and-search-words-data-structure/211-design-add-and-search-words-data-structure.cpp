class WordDictionary {
private:
    struct TrieNode 
    {
        bool isEnd = false;
        TrieNode *childs[26];
    };
    TrieNode *node;
    
public:
    WordDictionary()
    {
        node = new TrieNode();
    }

    bool search_pattern(TrieNode *tnode, string word, int idx)
    {
        TrieNode *curr = tnode;
        for (int i=idx; i<word.length(); i++)
        {
            char c = word[i];
            if (c == '.')
            {
                for (int j=0; j<26; j++)
                {
                    if (curr->childs[j])
                    {
                        if (i == word.length() - 1 && curr->childs[j]->isEnd)
                            return true;
                        
                        if (search_pattern(curr->childs[j], word, i + 1))
                            return true;   
                    }
                }
                return false;
            }
            
            if (curr->childs[c - 'a'] == NULL)
                return false;
            
            curr = curr->childs[c - 'a'];
        }
        return curr->isEnd;
    }
    
    bool search(string word)
    {
        return search_pattern(node, word, 0);
    }

    void addWord(string word)
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
};

/**
 * Your WordDictionary object will be instantiated and called as such:
 * WordDictionary* obj = new WordDictionary();
 * obj->addWord(word);
 * bool param_2 = obj->search(word);
 */