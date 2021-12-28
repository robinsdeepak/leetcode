/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode() : val(0), next(nullptr) {}
 *     ListNode(int x) : val(x), next(nullptr) {}
 *     ListNode(int x, ListNode *next) : val(x), next(next) {}
 * };
 */

class Solution {
public:

    ListNode* reverseKGroup(ListNode* head, int k) 
    {
        ListNode *node = head;
        
        int kc = k;
        
        while (kc && node)
        {
            node = node->next;
            kc--;            
        }
        
        if (kc > 0) return head;
        
        ListNode *prev = NULL;
        ListNode *next = NULL;
        ListNode *ptr = head;
        
        for (int i=0; i<k; i++)
        {
            next = ptr->next;
            ptr->next = prev;
            prev = ptr;
            ptr = next;
        }
        head->next = reverseKGroup(next, k);
        return prev;
    }
};
