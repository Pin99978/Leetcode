/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     struct ListNode *next;
 * };
 */

struct ListNode* reverseList(struct ListNode *head){

    struct ListNode *pre = NULL;
    struct ListNode *cur = head;
    struct ListNode *next = NULL;

    // do reverse
    while(cur){
        next = cur -> next;
        cur -> next = pre;
        pre = cur;
        cur = next;
    }
    return pre;
}


bool isPalindrome(struct ListNode* head) {
    
    // 
    if ( !head || !head -> next ) return true;


    // slow will go middle then return back
    struct ListNode *slow = head;
    
    //fast will go to the end
    struct ListNode *fast  = head;

    //
    struct ListNode *pre = NULL ;
    while ( fast && fast -> next ){
        fast = fast -> next ->next;
        slow = slow -> next ;
    }
    // now slow at the middle
    slow = reverseList(slow);
    while (slow){
        if (head-> val != slow -> val) return false;
        head =head ->next ;
        slow =slow ->next ;
    }
    return true;

}
