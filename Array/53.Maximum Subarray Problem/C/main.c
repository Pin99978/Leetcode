int maxSubArray(int* nums, int numsSize) {
    
    int cur_sum = 0;
    int max_sum = INT_MIN;

    for (int i =0 ; i < numsSize ; i++){

        // for each step , add nums to cur_sum
        cur_sum += nums[i];

        // 
        if ( max_sum < cur_sum ){
            max_sum = cur_sum;
        }

        if (cur_sum < 0){
            cur_sum = 0;
        }


    }

    return max_sum;
}
