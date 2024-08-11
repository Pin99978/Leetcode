int removeDuplicates(int* nums, int numsSize) {

    int *ptr = nums ;// point to ther 1st element 
    
    for (int *j = nums + 1 ; j < nums + numsSize  ; j ++ ){
        if ( *j != *ptr ){
            ptr++ ;
            *ptr = *j ;
        }
    }
    return ( ptr - nums ) + 1 ; 
}
