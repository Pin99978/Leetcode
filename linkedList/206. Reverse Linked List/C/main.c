/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     struct ListNode *next;
 * };
 */
struct ListNode* reverseList(struct ListNode* head) {
    
    if (head == NULL || head -> next == NULL)
        return head;

    // declare the pre Node 
    struct ListNode *preNode = NULL;

    // declare the cur Node , 
    struct ListNode *curNode = head ;

    // initial the nextnode 
    struct ListNode *nextNode ;

    while (curNode != NULL){

        nextNode = curNode -> next;
        curNode -> next = preNode;
        preNode = curNode;
        curNode = nextNode;
        
    }

    head = preNode;
    return preNode;
}
