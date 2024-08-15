/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     struct ListNode *next;
 * };
 */
struct ListNode* deleteDuplicates(struct ListNode* head) {
    
    struct ListNode *cur = head;
    // 
    if ( cur == NULL){
        return NULL;
    }
    struct ListNode *through = head -> next;
    while ( through != NULL ){

        if ( cur-> val != through->val){

             cur -> next = through ; 
             cur = through;
        }       

        through = through -> next;
       
    }
    cur -> next = NULL;
    return head ; 
}
