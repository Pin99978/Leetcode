/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     struct ListNode *next;
 * };
 */
struct ListNode* mergeTwoLists(struct ListNode* list1, struct ListNode* list2) {
   
    // Create the new list
    struct ListNode dummy ;
    struct ListNode *tail ; 
    tail = &dummy;

    // set the initial of dummy
    dummy.next = NULL;


    while ( list1 != NULL && list2 != NULL ){

        // Compare 2 linklist

        if ( list1 -> val <= list2  -> val ){
            
            tail -> next  = list1 ; 
            list1 = list1 -> next ;
        }else{

            tail -> next = list2 ;
            list2 = list2 -> next ;
        }
        tail  = tail  -> next ;
    }

    // check if the rest of list2 is done
    if ( list1 != NULL){
        tail -> next = list1 ;
    }else if(list2 != NULL) {
        tail -> next = list2 ; 
    }

    return dummy.next;
}
