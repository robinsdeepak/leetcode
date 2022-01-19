/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode(int x) : val(x), next(NULL) {}
 * };
 */
class Solution {
public:

    
    ListNode *detectCycle(ListNode *head) 
    {
        if (!head) return NULL;
        ListNode *fast = head->next;
        ListNode *slow = head;
        
        while (fast != slow)
        {
            if (!fast || !fast->next)
                return NULL;

            fast = fast->next->next;
            slow = slow->next;
        }
        
        int len = 1;
        fast = fast->next;
        while (fast != slow)
        {
            len++;
            fast = fast->next;
        }
        
        fast = head;
        slow = head;
        for (int i=0; i<len; i++)
            fast = fast->next;
        
        
        while (fast != slow)
        {
            fast = fast->next;
            slow = slow->next;
        }
        return fast;
    }
};
