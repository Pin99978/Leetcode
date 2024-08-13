

//Follow up: Could you write a solution that runs in O(m + n) time and use only O(1) memory?
// -> two pointers synchronization ( if two linked list no intersection , headA = headB = NULL 

/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     struct ListNode *next;
 * };
 */
struct ListNode *getIntersectionNode(struct ListNode *headA, struct ListNode *headB) {
    
    struct ListNode  *ptrA = headA;
    struct ListNode  *ptrB = headB;

    while ( ptrA != ptrB ){
        
        if ( ptrA == NULL) {
            ptrA = headB;
        }else{
            ptrA = ptrA -> next;
        }
        if ( ptrB ==NULL) {
            ptrB = headA;
        }else{
            ptrB = ptrB -> next;
        }
    }
    return ptrA;


}
