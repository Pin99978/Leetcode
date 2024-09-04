/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     struct ListNode *next;
 * };
 */
struct ListNode* addTwoNumbers(struct ListNode* l1, struct ListNode* l2) {
    
    // variable for handling ten_digit
    int if_tens_digit = 0 ; 

    struct ListNode *dummy = (struct ListNode*)malloc(sizeof(struct ListNode));
    dummy -> val = 0;
    dummy -> next = NULL;

    // create the cur which track of the last node in the result 
    // cur point to the head of dummy
    struct ListNode *cur = dummy;
    

    while (l1 != NULL || l2 != NULL || if_tens_digit != 0){

        // initial carry as last if_tens_digit
        int sum = if_tens_digit;

        if ( l1 ){
            sum += l1 -> val;
            l1 = l1 -> next;
        }
        if (l2){
            sum += l2 ->val;
            l2 = l2-> next;
        }

        if_tens_digit = sum / 10; 
        int digit = sum % 10;

        cur -> next = (struct ListNode *)malloc(sizeof(struct ListNode));
        cur -> next -> val = digit;
        cur -> next -> next = NULL;
        
        cur =cur -> next ;

    }
    return dummy -> next;
}
