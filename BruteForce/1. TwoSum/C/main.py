/**
 * Note: The returned array must be malloced, assume caller calls free().
 */
int* twoSum(int* nums, int numsSize, int target, int* returnSize) {

    // using the brute force with 2-d array 
    // practice C pointer 

    int *ans = (int*)malloc(2 * sizeof(int));
    if (ans == NULL){
        *returnSize = 0;
        return NULL;
    }

    *returnSize = 2;

    for ( int i = 0 ; i < numsSize ; i ++){

        int others = target - *( nums + i );
       
        for ( int j = i + 1  ; j  < numsSize ; j++){
            if ( others == *(nums+j) ){

                ans[0] = i;
                ans[1] = j;
                return ans;
            }
        }
    }
    free(ans);
    *returnSize = 0;
    return NULL;
}
