#include <stdio.h>

//Problem Statement:

/* Given an integer n and a position k, toggle the K-th bit of n and return the result. Toggling means changing a 0 to 1 or a 1 to 0 in the binary representation of the number.
*/


int check_kth_bit(int n, int k){
    int mask = 1 << (k-1); // mask creating
    return  n & mask;  // check the kth bit of n // if the bit is set then return the number , otherwise return 0;
}

int set_kth_bit(int n, int k){
    int mask = 1 << (k-1); // mask creating
    return n & mask; // set the kth bit of n
}

int toggle_kth_bit( int n , int k){

    int mask = 1 << (k-1) ;

    return  n ^  mask;  // toggle the kth bit of n 
}

int clean_kth_bit(int n, int k){
    int mask = 1 << (k-1); // mask creating
    return n & ~mask; // clear the kth bit of n
}

int main(){

    int n , k;
    printf("Enter the number: ");
    scanf("%d",&n);
    printf("Enter the position: ");
    scanf("%d",&k);
    return ;
}

// * we can also use the mask to do 
// Bit Checking -> number & mask
// Bit Setting  -> number | mask
// Bit toggling -> number ^ mask
// Bit Clearing -> number & ~mask
