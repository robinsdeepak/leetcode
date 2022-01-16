class node
{
    public:
    int key;
    int val;
    node *prev;
    node *next;
    node(int _key,int _val)
    {
        key=_key;
        val=_val;
    }
};

class LRUCache {
public:
    
    int capacity;
    int size = 0;
    node *head = new node(-1, -1);
    node *tail = new node(-1, -1);

    unordered_map<int,node*> m;

    LRUCache(int x) 
    {
        capacity = x;
        head->next = tail;
        tail->prev = head;
    }
    
    int get(int key) 
    {
        if (!m.count(key))
            return -1;
        
        node *tmp = m[key];
        
        if (size > 1)
        {
            node *prev = tmp->prev;
            node *next = tmp->next;
            
            prev->next = tmp->next;
            next->prev = tmp->prev;
            
            node *tnext = head->next;
            
            head->next = tmp;
            tnext->prev = tmp;
            
            tmp->next = tnext;
            tmp->prev = head;
        }
        return tmp->val;
    }
    
    node* pop(int key)
    {
        node *n = m[key];
        node *prev = n->prev;
        node *next = n->next;
        prev->next = next;
        next->prev = prev;
        m.erase(m.find(key));
        return n;
        // delete n;
    }
    
    void put(int key, int value) 
    {
        node *curr;
        if (m.count(key))
        {
            curr = pop(key);
            curr->val = value;
        }
        else if (size == capacity)
        {
            node *lru = tail->prev;
            curr = pop(lru->key);
            curr->key = key;
            curr->val = value;
        }
        else
        {
            curr = new node(key, value);
            size++;
        }

        node *first = head->next;
        head->next = curr;
        curr->prev = head;
        curr->next = first;
        first->prev = curr;
        m[key] = curr;   
    }
};



/**
 * Your LRUCache object will be instantiated and called as such:
 * LRUCache* obj = new LRUCache(capacity);
 * int param_1 = obj->get(key);
 * obj->put(key,value);
 */

